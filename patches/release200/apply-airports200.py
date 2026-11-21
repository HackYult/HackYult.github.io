"""Apply the reviewed release 200 overlay to an isolated release 199 build."""
from pathlib import Path
import base64
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile


root = Path('.')
dist = root / 'dist'
bundle = json.loads(gzip.decompress(base64.b64decode(Path('source200.b64').read_text())))
assert bundle['schema'] == 200, 'Unexpected overlay schema'
manifest = json.loads((dist / 'data/render-release.json').read_text())
assert manifest['version'] == 199, 'Release 200 requires the deployed release 199 baseline'


def relative_path(name):
    path = Path(name)
    assert name and not path.is_absolute() and '..' not in path.parts, name
    return path


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


pending = {}
# Check every source patch before writing any source file. Only module version
# suffixes are canonicalized; unrelated data URL changes must match the baseline.
for name, patch in bundle.get('patches', {}).items():
    path = relative_path(name)
    original = re.sub(r'(?<=\.js)\?v=[0-9.]+', '', (dist / path).read_text())
    assert sha(original) == patch['before'], 'Baseline mismatch: ' + name
    previous_end = 0
    for start, end, replacement in patch['ops']:
        assert isinstance(start, int) and isinstance(end, int)
        assert previous_end <= start <= end <= len(original), 'Invalid patch range: ' + name
        assert isinstance(replacement, str)
        previous_end = end
    changed = original
    for start, end, replacement in reversed(patch['ops']):
        changed = changed[:start] + replacement + changed[end:]
    assert sha(changed) == patch['after'], 'Patched hash mismatch: ' + name
    pending[name] = changed

for name, text in bundle.get('files', {}).items():
    relative_path(name)
    assert name not in pending and isinstance(text, str), 'Duplicate overlay path: ' + name
    pending[name] = text

for name, text in pending.items():
    target = dist / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)

args = [sys.executable, 'scripts/import-major-airports199.py', '--release','200']
if os.environ.get('AERONAUT_MAJOR_SOURCE'):
    args += ['--upstream', os.environ['AERONAUT_MAJOR_SOURCE']]
subprocess.run(args, cwd=dist, check=True)
subprocess.run([sys.executable, 'scripts/extend-airports200.py'], cwd=dist, check=True)
subprocess.run([sys.executable, 'tests/open-airports200.test.py'], cwd=dist, check=True)

manifest.update(version=200, terminalAssets=200, openTerminalRevision=200)
release_text = json.dumps(manifest) + '\n'
(dist / 'data/render-release.json').write_text(release_text)
(root / 'data/render-release.json').write_text(release_text)
pending['data/render-release.json'] = ''
subprocess.run([sys.executable, 'scripts/version-runtime.py'], check=True)

# The overlay author can include the focused runtime regression suite alongside
# the mandatory original-asset checks, without adding arbitrary shell commands.
node_tests = bundle.get('nodeTests', [])
for name in node_tests:
    path = relative_path(name)
    assert path.parts[0] == 'tests' and path.suffix in ('.js', '.mjs'), name
if node_tests:
    subprocess.run(['node', '--test', *node_tests], cwd=dist, check=True)

pending['data/airports.json'] = ''
pending['assets/geographic-models/catalog.json'] = ''
for folder in [*(dist / 'assets/geographic-models').glob('open200-*'), dist / 'reports/release200']:
    for path in folder.rglob('*'):
        if path.is_file():
            pending[str(path.relative_to(dist))] = ''

source = dist / 'sources/game-source.zip'
temporary = source.with_suffix('.200.zip')
with zipfile.ZipFile(source) as old, zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED) as new:
    for item in old.infolist():
        if item.filename not in pending:
            new.writestr(item, old.read(item.filename))
    for name in sorted(pending):
        new.write(dist / name, name)
temporary.replace(source)
print('Release 200: original airport source models, reviewed runtime improvements, and corresponding source packaged;', len(pending), 'files')
