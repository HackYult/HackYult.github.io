"""Add independent rudder pedals and pitch trim to release 205."""
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
assert manifest['version'] == 205
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
manifest.update(version=206, flightControlRevision=206)
release = json.dumps(manifest) + '\n'
manifest_path.write_text(release)
Path('data/render-release.json').write_text(release)
subprocess.run([sys.executable, 'scripts/version-runtime.py'], check=True)
subprocess.run(['node','--test','tests/manual-axes206.test.mjs','tests/gear-view205.test.mjs','tests/dreamliner-trucks203.test.mjs','tests/airframe-approach202.test.mjs'], cwd=dist, check=True)
changed = [*(dist / name for name in files), manifest_path]
names = {str(p.relative_to(dist)) for p in changed}
source = dist/'sources/game-source.zip'
tmp = source.with_suffix('.206.zip')
with zipfile.ZipFile(source) as old, zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED) as new:
    for item in old.infolist():
        if item.filename not in names:
            new.writestr(item, old.read(item.filename))
    for path in changed:
        new.write(path, str(path.relative_to(dist)))
tmp.replace(source)
