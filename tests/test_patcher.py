import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import kawaii_pylance as kp


def fixture_locale():
    return {'CallHierarchy': {'library': '库', 'standardLibrary': '标准库'},
            'Diagnostic': {'symbolIsUndefined': '未定义“{name}”',
                           'importResolveFailure': '无法解析导入“{importName}”',
                           'expectedCloseBrace': '"{" 未关闭',
                           'example': '路径 C:\\new\\test，单引号\'，换行\n{type}'},
            'DiagnosticAddendum': {'detail': '原始补充 {name}'},
            'CodeAction': {'create': '原始操作'}}


CONFIG = {'schemaVersion': 1, 'locale': 'zh-cn', 'fallbackPrefixes': ['呜…'],
          'Diagnostic': {'symbolIsUndefined': '笨蛋！“{name}”还没定义呀'}}


def bundle(locale, single=False):
    inner = json.dumps(locale, ensure_ascii=False, separators=(',', ':'))
    if single:
        outer = "'" + inner.replace('\\', '\\\\').replace("'", "\\'") + "'"
    else:
        outer = json.dumps(inner, ensure_ascii=False)
    return ('/* untouched prefix */ const zh=JSON.parse(' + outer
            + '); /* untouched suffix */').encode()


class PatcherTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'dist').mkdir()
        (self.root / 'package.json').write_text(json.dumps(
            {'publisher': 'ms-python', 'name': 'vscode-pylance', 'version': 'fixture'}))
        self.data = bundle(fixture_locale(), single=True)
        for name in ['pyright', 'browser.async']:
            (self.root / f'dist/{name}.bundle.js').write_bytes(self.data)

    def tearDown(self):
        self.temp.cleanup()

    def run_quiet(self, func, *args, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return func(*args, **kwargs)

    def test_safe_data_decoder(self):
        self.assertEqual(kp.decode_js_string(r"'a\x41\u4f60\u{1f431}\n\'\\'"), "aA你🐱\n'\\")

    def test_single_and_double_quoted_bundles(self):
        for single in (True, False):
            data = bundle(fixture_locale(), single)
            output, original, localized = kp.patch_bytes(data, CONFIG)
            self.assertEqual(localized['Diagnostic']['symbolIsUndefined'], CONFIG['Diagnostic']['symbolIsUndefined'])
            self.assertEqual(localized['DiagnosticAddendum'], original['DiagnosticAddendum'])
            self.assertEqual(localized['CodeAction'], original['CodeAction'])
            self.assertEqual(kp.find_locale(output.decode())[1], localized)
            self.assertTrue(output.startswith(b'/* untouched prefix */'))
            self.assertTrue(output.endswith(b'/* untouched suffix */'))

    def test_other_locales_untouched(self):
        other = fixture_locale()
        other['CallHierarchy']['library'] = 'Library'
        data = bundle(other) + b';' + self.data
        result = kp.patch_bytes(data, CONFIG)[0]
        self.assertTrue(result.startswith(bundle(other)))

    def test_duplicate_locale_refused(self):
        with self.assertRaises(kp.PatchError):
            kp.patch_bytes(self.data + b';' + self.data, CONFIG)

    def test_placeholder_loss_and_duplication_refused(self):
        for value in ('没定义呀', '{name} {name}'):
            config = copy.deepcopy(CONFIG)
            config['Diagnostic']['symbolIsUndefined'] = value
            with self.assertRaises(kp.PatchError):
                kp.patch_bytes(self.data, config)

    def test_unknown_key_refused(self):
        config = copy.deepcopy(CONFIG)
        config['Diagnostic']['notAnUpstreamKey'] = '不存在'
        with self.assertRaises(kp.PatchError):
            kp.patch_bytes(self.data, config)

    def test_primary_and_pylance_specific_dict_in_same_bundle(self):
        extra = {'Messages': {'defaultPythonEnvironmentName': '默认 Python 环境'},
                 'Diagnostic': {'importResolveNoEnvironment': '找不到“{importName}”',
                                'importResolveRedirect': '环境“{venv}”找不到“{importName}”'},
                 'CodeAction': {'create': '原始操作'}}
        config = copy.deepcopy(CONFIG)
        config['PylanceDiagnostic'] = {
            'importResolveNoEnvironment': '呜…找不到“{importName}”',
            'importResolveRedirect': '呜…“{venv}”找不到“{importName}”'}
        data = self.data + b';const extra=' + bundle(extra)
        output = kp.patch_bytes(data, config)[0].decode()
        self.assertEqual(kp.find_locale(output)[1]['Diagnostic']['symbolIsUndefined'],
                         CONFIG['Diagnostic']['symbolIsUndefined'])
        localized_extra = kp.find_pylance_locale(output)[1]
        self.assertEqual(localized_extra['Diagnostic'], config['PylanceDiagnostic'])
        self.assertEqual(localized_extra['CodeAction'], extra['CodeAction'])

    def test_dry_run_has_no_writes(self):
        self.run_quiet(kp.apply, self.root, CONFIG, True)
        self.assertFalse((self.root / kp.BACKUP).exists())
        self.assertEqual((self.root / 'dist/pyright.bundle.js').read_bytes(), self.data)

    def test_apply_idempotence_and_exact_restore(self):
        self.run_quiet(kp.apply, self.root, CONFIG)
        first = (self.root / 'dist/pyright.bundle.js').read_bytes()
        self.run_quiet(kp.apply, self.root, CONFIG)
        self.assertEqual(first, (self.root / 'dist/pyright.bundle.js').read_bytes())
        self.run_quiet(kp.restore, self.root)
        for file in (self.root / 'dist').glob('*.js'):
            self.assertEqual(file.read_bytes(), self.data)
        self.assertFalse((self.root / kp.BACKUP).exists())

    def test_changed_config_refused(self):
        self.run_quiet(kp.apply, self.root, CONFIG)
        config = copy.deepcopy(CONFIG)
        config['fallbackPrefixes'] = ['欸？']
        with self.assertRaises(kp.PatchError):
            self.run_quiet(kp.apply, self.root, config)

    def test_conflict_prevents_all_restore_writes(self):
        self.run_quiet(kp.apply, self.root, CONFIG)
        path = self.root / 'dist/pyright.bundle.js'
        path.write_bytes(b'changed by an extension update')
        before = {p.name: p.read_bytes() for p in (self.root / 'dist').glob('*.js')}
        with self.assertRaises(kp.PatchError):
            self.run_quiet(kp.restore, self.root)
        self.assertEqual(before, {p.name: p.read_bytes() for p in (self.root / 'dist').glob('*.js')})

    def test_corrupt_backup_refused(self):
        self.run_quiet(kp.apply, self.root, CONFIG)
        (self.root / kp.BACKUP / 'pyright.bundle.js').write_bytes(b'corrupt')
        with self.assertRaises(kp.PatchError):
            self.run_quiet(kp.restore, self.root)
        with self.assertRaises(kp.PatchError):
            self.run_quiet(kp.apply, self.root, CONFIG)

    def test_invalid_manifest_path_refused(self):
        self.run_quiet(kp.apply, self.root, CONFIG)
        path = self.root / kp.BACKUP / 'manifest.json'
        manifest = kp.load_json(path)
        manifest['files'][0]['relative'] = '../outside.js'
        path.write_text(json.dumps(manifest))
        with self.assertRaises(kp.PatchError):
            self.run_quiet(kp.restore, self.root)

    def test_apply_failure_rolls_back_written_bundles(self):
        real_write = kp.atomic_write
        def fail_on_second_bundle(path, data):
            if path == self.root / 'dist/pyright.bundle.js' and data != self.data:
                raise OSError('injected write failure')
            return real_write(path, data)
        with patch.object(kp, 'atomic_write', side_effect=fail_on_second_bundle):
            with self.assertRaises(OSError):
                self.run_quiet(kp.apply, self.root, CONFIG)
        for file in (self.root / 'dist').glob('*.js'):
            self.assertEqual(file.read_bytes(), self.data)
        # The prepared manifest permits a later restore after interruption.
        self.run_quiet(kp.restore, self.root)


if __name__ == '__main__':
    unittest.main()
