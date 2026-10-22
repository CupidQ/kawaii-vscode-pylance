import json
from pathlib import Path
import re
import unittest
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
CPP_PARAMETER = re.compile(r'%[A-Za-z]+\d*')


class DiagnosticCopyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT / 'patches/zh-cn.json').read_text(encoding='utf-8'))
        cls.provenance = json.loads((ROOT / 'patches/cpp-reuse.json').read_text(encoding='utf-8'))

    def test_cpp_attribution_tracks_actual_patch(self):
        entries = self.provenance['entries']
        self.assertEqual(len(entries), len({(r['section'], r['key']) for r in entries}))
        self.assertEqual(dict(Counter(r['mode'] for r in entries)), self.provenance['countsByMode'])
        for record in entries:
            with self.subTest(key=record['key']):
                self.assertEqual(self.config[record['section']][record['key']], record['message'])
                self.assertGreaterEqual(record['sourceIndex'], 0)
                self.assertLess(record['sourceIndex'], self.provenance['sourceEntryCount'])

    def test_exact_reuse_and_placeholder_only_reuse_are_honest(self):
        for record in self.provenance['entries']:
            with self.subTest(key=record['key']):
                if record['mode'] == '原句沿用':
                    self.assertEqual(record['sourceMessage'], record['message'])
                elif record['mode'] == '占位符替换':
                    parts = CPP_PARAMETER.split(record['sourceMessage'])
                    pattern = '.+?'.join(re.escape(part) for part in parts)
                    self.assertRegex(record['message'], '^' + pattern + '$')

    def test_no_cpp_formatter_tokens_leak_into_python_messages(self):
        for section in ['Diagnostic', 'PylanceDiagnostic']:
            for key, message in self.config[section].items():
                with self.subTest(key=key):
                    self.assertIsNone(CPP_PARAMETER.search(message))

    def test_previous_review_semantic_regressions_are_fixed(self):
        one_more = self.config['Diagnostic']['argMorePositionalExpectedOne']
        self.assertIn('1', one_more)
        self.assertNotIn('至少', one_more)
        self.assertIn('不允许', self.config['Diagnostic']['yieldWithinComprehension'])
        self.assertNotIn('给多了', self.config['Diagnostic']['staticClsSelfParam'])
        self.assertNotIn('开关', self.config['Diagnostic']['breakOutsideLoop'])
        for key in ['finallyBreak', 'finallyContinue', 'finallyReturn']:
            self.assertIn('退出 finally', self.config['Diagnostic'][key])


if __name__ == '__main__':
    unittest.main()
