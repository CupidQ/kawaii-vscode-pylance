#!/usr/bin/env python3
"""Local, reversible zh-cn diagnostic patcher. Python 3.10+, standard library only."""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
BACKUP = '.kawaii-pylance-backup'
PARSE_CALL = re.compile(r'''JSON\.parse\((?P<literal>'(?:\\.|[^'\\])*'|"(?:\\.|[^"\\])*")\)''', re.S)
PLACEHOLDER = re.compile(r'\{[A-Za-z_]\w*\}')


class PatchError(Exception):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def decode_js_string(literal: str) -> str:
    """Decode a quoted JS data string without eval or executing bundle code."""
    chars = []
    i = 1
    escapes = {'n': '\n', 'r': '\r', 't': '\t', 'b': '\b', 'f': '\f',
               'v': '\v', '0': '\0', "'": "'", '"': '"', '\\': '\\', '/': '/'}
    while i < len(literal) - 1:
        c = literal[i]
        i += 1
        if c != '\\':
            chars.append(c)
            continue
        c = literal[i]
        i += 1
        if c in escapes:
            chars.append(escapes[c])
        elif c in ('x', 'u'):
            if c == 'u' and literal[i:i + 1] == '{':
                end = literal.index('}', i)
                chars.append(chr(int(literal[i + 1:end], 16)))
                i = end + 1
            else:
                size = 2 if c == 'x' else 4
                chars.append(chr(int(literal[i:i + size], 16)))
                i += size
        elif c == '\n':
            pass
        elif c == '\r':
            i += literal[i:i + 1] == '\n'
        else:
            raise PatchError(f'Unsupported JS escape: {c!r}')
    return ''.join(chars)


def find_locale(text: str):
    found = []
    for match in PARSE_CALL.finditer(text):
        try:
            obj = json.loads(decode_js_string(match['literal']))
        except (ValueError, PatchError):
            continue
        if (isinstance(obj, dict) and isinstance(obj.get('Diagnostic'), dict)
                and obj.get('CallHierarchy', {}).get('library') == '库'
                and obj.get('CallHierarchy', {}).get('standardLibrary') == '标准库'
                and 'importResolveFailure' in obj['Diagnostic']
                and 'symbolIsUndefined' in obj['Diagnostic']):
            found.append((match, obj))
    if len(found) > 1:
        raise PatchError('More than one simplified Chinese locale in a bundle; refusing ambiguous patch.')
    return found[0] if found else None


def validate_config(config):
    if (config.get('schemaVersion') != 1 or config.get('locale') != 'zh-cn'
            or not isinstance(config.get('Diagnostic'), dict)):
        raise PatchError('Expected schemaVersion=1, locale=zh-cn and a Diagnostic object.')
    prefixes = config.get('fallbackPrefixes')
    if not isinstance(prefixes, list) or not prefixes or not all(isinstance(x, str) and x for x in prefixes):
        raise PatchError('fallbackPrefixes must be a nonempty list of nonempty strings.')
    if any(PLACEHOLDER.search(x) for x in prefixes):
        raise PatchError('fallbackPrefixes cannot introduce placeholders.')
    if not all(isinstance(k, str) and isinstance(v, str) and v for k, v in config['Diagnostic'].items()):
        raise PatchError('Every Diagnostic entry must be a nonempty string.')
    extra = config.get('PylanceDiagnostic', {})
    if not isinstance(extra, dict) or not all(isinstance(v, str) and v for v in extra.values()):
        raise PatchError('PylanceDiagnostic must contain nonempty strings.')


def find_pylance_locale(text: str):
    found = []
    for match in PARSE_CALL.finditer(text):
        try:
            obj = json.loads(decode_js_string(match['literal']))
        except (ValueError, PatchError):
            continue
        if (isinstance(obj, dict) and isinstance(obj.get('Diagnostic'), dict)
                and obj.get('Messages', {}).get('defaultPythonEnvironmentName') == '默认 Python 环境'
                and 'importResolveNoEnvironment' in obj['Diagnostic']
                and 'importResolveRedirect' in obj['Diagnostic']):
            found.append((match, obj))
    if len(found) > 1:
        raise PatchError('Multiple Pylance-specific zh-cn dictionaries found; refusing ambiguous patch.')
    return found[0] if found else None


def transform(locale, config, section='Diagnostic'):
    # Deep copy the locale, including addenda and unrelated UI strings.
    output = json.loads(json.dumps(locale, ensure_ascii=True))
    diagnostics = output['Diagnostic']
    custom = config.get(section, {})
    missing = set(custom) - set(diagnostics)
    if missing:
        raise PatchError('This Pylance dictionary lacks configured keys: ' + ', '.join(sorted(missing)))
    for key, original in diagnostics.items():
        if not isinstance(original, str):
            raise PatchError(f'Unsupported diagnostic value for {key}.')
        replacement = custom.get(key)
        if replacement is None:
            prefixes = config['fallbackPrefixes']
            index = int(hashlib.sha256(key.encode()).hexdigest()[:8], 16) % len(prefixes)
            replacement = prefixes[index] + original
        if Counter(PLACEHOLDER.findall(original)) != Counter(PLACEHOLDER.findall(replacement)):
            raise PatchError(f'Placeholder mismatch: Diagnostic.{key}')
        diagnostics[key] = replacement
    return output


def patch_bytes(data: bytes, config):
    text = data.decode('utf-8')
    results = [(find_locale(text), 'Diagnostic'), (find_pylance_locale(text), 'PylanceDiagnostic')]
    found = [(result, section) for result, section in results if result is not None]
    if not found:
        return None
    replacements = []
    for (match, locale), section in found:
        output = transform(locale, config, section)
        # JSON string literals are also valid JavaScript literals. No eval is used.
        encoded = json.dumps(json.dumps(output, ensure_ascii=False, separators=(',', ':')),
                             ensure_ascii=False).replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        replacements.append((match, locale, output, encoded, section))
    patched = text
    for match, _, _, encoded, _ in sorted(replacements, key=lambda r: r[0].start(), reverse=True):
        start, end = match.span('literal')
        patched = patched[:start] + encoded + patched[end:]
    for _, _, output, _, section in replacements:
        finder = find_locale if section == 'Diagnostic' else find_pylance_locale
        recovered = finder(patched)
        if recovered is None or recovered[1] != output:
            raise PatchError('Patched dictionary failed its round-trip verification.')
    # Prefer the primary dictionary when both appear in one bundle.
    return patched.encode('utf-8'), replacements[0][1], replacements[0][2]


def find_extension(explicit: str | None) -> Path:
    if explicit:
        root = Path(explicit).expanduser().resolve()
    else:
        candidates = []
        for folder in (Path.home() / '.vscode/extensions', Path.home() / '.vscode-insiders/extensions'):
            if folder.is_dir():
                candidates.extend(p for p in folder.glob('ms-python.vscode-pylance-*')
                                  if p.is_dir() and (p / 'package.json').is_file())
        if len(candidates) != 1:
            choices = '\n'.join(str(p) for p in candidates) or '(none)'
            raise PatchError('Specify --extension; found zero or multiple Pylance installations:\n' + choices)
        root = candidates[0].resolve()
    package = load_json(root / 'package.json')
    if package.get('publisher') != 'ms-python' or package.get('name') != 'vscode-pylance':
        raise PatchError('The selected folder is not ms-python.vscode-pylance.')
    if not (root / 'dist/pyright.bundle.js').is_file():
        raise PatchError('Unsupported Pylance layout: dist/pyright.bundle.js is missing.')
    return root


def plan_patch(root: Path, config):
    plan = []
    for path in sorted((root / 'dist').glob('*.bundle.js')):
        original = path.read_bytes()
        result = patch_bytes(original, config)
        if result:
            patched, locale, output = result
            plan.append({'relative': path.relative_to(root).as_posix(),
                         'original': original, 'patched': patched, 'locale': locale,
                         'output': output})
    primary = next((x for x in plan if x['relative'] == 'dist/pyright.bundle.js'), None)
    if primary is None or find_locale(primary['original'].decode('utf-8')) is None:
        raise PatchError('The expected zh-cn dictionary was not found in pyright.bundle.js. Nothing was changed.')
    return plan


def atomic_write(path: Path, data: bytes):
    fd, temp_name = tempfile.mkstemp(prefix='.kawaii-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def save_manifest(folder: Path, manifest):
    atomic_write(folder / 'manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2).encode('utf-8'))


@contextmanager
def exclusive(folder: Path):
    folder.mkdir(exist_ok=True)
    lock = folder / 'operation.lock'
    try:
        fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    except FileExistsError as exc:
        raise PatchError('Another patch operation is running (or left an operation.lock).') from exc
    os.close(fd)
    try:
        yield
    finally:
        lock.unlink()


def checked_entries(root: Path, manifest):
    if manifest.get('schemaVersion') != 1 or not isinstance(manifest.get('files'), list):
        raise PatchError('Invalid backup manifest.')
    entries = manifest['files']
    names = []
    for entry in entries:
        name = entry['relative']
        if not re.fullmatch(r'dist/[A-Za-z0-9._-]+\.bundle\.js', name):
            raise PatchError('Invalid backup path.')
        target = (root / name).resolve()
        if target.parent != (root / 'dist').resolve():
            raise PatchError('Backup path escapes the extension.')
        names.append(name)
    if not entries or len(names) != len(set(names)):
        raise PatchError('Empty or duplicate backup entries.')
    return entries


def apply(root: Path, config, dry_run=False):
    folder = root / BACKUP
    manifest_path = folder / 'manifest.json'
    config_hash = sha(json.dumps(config, sort_keys=True, ensure_ascii=True).encode())
    if manifest_path.exists():
        manifest = load_json(manifest_path)
        entries = checked_entries(root, manifest)
        for entry in entries:
            backup_path = folder / Path(entry['relative']).name
            if not backup_path.is_file() or sha(backup_path.read_bytes()) != entry['originalSha256']:
                raise PatchError('Existing backup is missing or damaged: ' + entry['relative'])
        if manifest['configSha256'] == config_hash and all(
                sha((root / e['relative']).read_bytes()) == e['patchedSha256'] for e in entries):
            print('Already applied; no files changed.')
            return
        raise PatchError('An existing backup or changed patch was found. Run status, then restore before reapplying.')
    plan = plan_patch(root, config)
    print(f'Pylance {load_json(root / "package.json")["version"]}: {root}')
    primary = next(x for x in plan if x['relative'] == 'dist/pyright.bundle.js')
    print(f'{len(plan)} bundles; {len(primary["locale"]["Diagnostic"])} primary diagnostic entries; '
          f'{len(config["Diagnostic"])} custom primary messages.')
    for item in plan:
        print(('Would patch: ' if dry_run else 'Patch: ') + item['relative'])
    if dry_run:
        print('Dry run complete; no files changed.')
        return
    with exclusive(folder):
        if manifest_path.exists():
            raise PatchError('Backup appeared during planning. Run status before retrying.')
        manifest = {'schemaVersion': 1, 'state': 'preparing',
                    'pylanceVersion': load_json(root / 'package.json')['version'],
                    'configSha256': config_hash, 'files': []}
        for item in plan:
            target = root / item['relative']
            if target.read_bytes() != item['original']:
                raise PatchError('Extension files changed during planning. Close VS Code and retry.')
            backup_path = folder / Path(item['relative']).name
            if backup_path.exists():
                raise PatchError('Untracked backup found; preserve it before retrying: ' + str(backup_path))
            backup_path.write_bytes(item['original'])
            manifest['files'].append({'relative': item['relative'],
                                      'originalSha256': sha(item['original']),
                                      'patchedSha256': sha(item['patched'])})
        save_manifest(folder, manifest)
        try:
            for item in plan:
                target = root / item['relative']
                if target.read_bytes() != item['original']:
                    raise PatchError('Extension changed during apply; refusing overwrite.')
                atomic_write(target, item['patched'])
            manifest['state'] = 'applied'
            save_manifest(folder, manifest)
        except Exception:
            # Restore only bytes written by us; preserve external modifications.
            for item in plan:
                target = root / item['relative']
                if target.read_bytes() == item['patched']:
                    atomic_write(target, item['original'])
            raise
    print('Applied and backed up. Restart VS Code to load the new messages.')


def restore(root: Path):
    folder = root / BACKUP
    manifest_path = folder / 'manifest.json'
    if not manifest_path.exists():
        raise PatchError('No patch backup was found.')
    with exclusive(folder):
        manifest = load_json(manifest_path)
        entries = checked_entries(root, manifest)
        restore_plan = []
        for entry in entries:
            target = root / entry['relative']
            original = (folder / Path(entry['relative']).name).read_bytes()
            if sha(original) != entry['originalSha256']:
                raise PatchError('Backup hash mismatch: ' + entry['relative'])
            current = target.read_bytes()
            if sha(current) not in (entry['originalSha256'], entry['patchedSha256']):
                raise PatchError('File changed externally; refusing to overwrite: ' + entry['relative'])
            restore_plan.append((target, current, original))
        # Persist a recoverable state before the first mutation.
        manifest['state'] = 'restoring'
        save_manifest(folder, manifest)
        for target, expected, original in restore_plan:
            if target.read_bytes() != expected:
                raise PatchError('File changed during restore; backup retained.')
            atomic_write(target, original)
        # Exact allowlisted files only; never recursively delete the directory.
        manifest_path.unlink()
        for entry in entries:
            (folder / Path(entry['relative']).name).unlink()
    try:
        folder.rmdir()
    except OSError:
        pass
    print('Restored original bytes; SHA-256 verified. Restart VS Code.')


def status(root: Path):
    print(f'Pylance {load_json(root / "package.json")["version"]}: {root}')
    manifest_path = root / BACKUP / 'manifest.json'
    if not manifest_path.exists():
        print('No backup manifest (not managed by this patcher).')
        return
    manifest = load_json(manifest_path)
    print('Manifest state:', manifest.get('state'))
    for entry in checked_entries(root, manifest):
        current = sha((root / entry['relative']).read_bytes())
        label = ('patched' if current == entry['patchedSha256'] else
                 'original' if current == entry['originalSha256'] else 'CONFLICT: externally changed')
        backup = root / BACKUP / Path(entry['relative']).name
        backup_ok = backup.is_file() and sha(backup.read_bytes()) == entry['originalSha256']
        print(f'{entry["relative"]}: {label}; backup={"OK" if backup_ok else "INVALID"}')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['status', 'preview', 'apply', 'restore', 'export'])
    parser.add_argument('--extension', help='Full path to ms-python.vscode-pylance-VERSION')
    parser.add_argument('--patch', type=Path, default=ROOT / 'patches/zh-cn.json')
    parser.add_argument('--dry-run', action='store_true', help='Plan apply without writing anything')
    parser.add_argument('--limit', type=int, default=12, help='Number of custom messages to preview')
    parser.add_argument('--output', type=Path, help='Destination for export; refuses existing files')
    args = parser.parse_args(argv)
    try:
        root = find_extension(args.extension)
        if args.command == 'status':
            status(root)
        elif args.command == 'restore':
            restore(root)
        else:
            config = load_json(args.patch)
            validate_config(config)
            if args.command == 'apply':
                apply(root, config, args.dry_run)
            else:
                if (root / BACKUP / 'manifest.json').exists():
                    raise PatchError('Preview/export requires an unpatched copy; restore first to avoid double styling.')
                plan = plan_patch(root, config)
                item = next(x for x in plan if x['relative'] == 'dist/pyright.bundle.js')
                if args.command == 'export':
                    if args.output is None:
                        raise PatchError('export requires --output FILE.json')
                    # An export is for inspection, not an external locale file Pylance can load.
                    with args.output.open('x', encoding='utf-8') as stream:
                        json.dump(item['output'], stream, ensure_ascii=False, indent=2)
                    print('Exported for inspection:', args.output.resolve())
                else:
                    for key in list(config['Diagnostic'])[:max(0, args.limit)]:
                        print(key + '\n  Before: ' + item['locale']['Diagnostic'][key]
                              + '\n  After:  ' + item['output']['Diagnostic'][key])
                    print(f'{len(item["locale"]["Diagnostic"])} total; {len(config["Diagnostic"])} custom; '
                          'remaining primary messages receive a prefix. Addenda/UI stay original.')
        return 0
    except (PatchError, OSError, ValueError, KeyError, TypeError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
