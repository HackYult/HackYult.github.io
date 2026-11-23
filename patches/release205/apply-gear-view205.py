"""Add the main landing gear inspection camera to the release 204 Pages build."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

dist = Path('dist')
manifest_path = dist / 'data/render-release.json'
manifest = json.loads(manifest_path.read_text())
assert manifest['version'] == 204
import gzip, base64
files = json.loads(gzip.decompress(base64.b64decode('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')))
outputs = {}
for name, (expected, edits) in files.items():
    path = dist / name
    if expected:
        baseline = re.sub(r'(?<=\.js)\?v=[0-9.]+', '', path.read_text())
        assert hashlib.sha256(baseline.encode()).hexdigest() == expected, name
        lines = baseline.splitlines(True)
        for start, end, replacement in reversed(edits):
            lines[start:end] = [replacement]
        outputs[name] = ''.join(lines)
    else:
        outputs[name] = edits
for name, text in outputs.items():
    (dist / name).write_text(text)
manifest.update(version=205, gearCameraRevision=205)
release = json.dumps(manifest) + '\n'
manifest_path.write_text(release)
Path('data/render-release.json').write_text(release)
subprocess.run([sys.executable, 'scripts/version-runtime.py'], check=True)
subprocess.run(['node','--test','tests/gear-view205.test.mjs','tests/dreamliner-trucks203.test.mjs','tests/airframe-approach202.test.mjs'], cwd=dist, check=True)
changed = [*(dist / name for name in files), manifest_path]
names = {str(p.relative_to(dist)) for p in changed}
source = dist/'sources/game-source.zip'
tmp = source.with_suffix('.205.zip')
with zipfile.ZipFile(source) as old, zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED) as new:
    for item in old.infolist():
        if item.filename not in names:
            new.writestr(item, old.read(item.filename))
    for path in changed:
        new.write(path, str(path.relative_to(dist)))
tmp.replace(source)
