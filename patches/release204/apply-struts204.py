"""Install weight-dependent landing gear on the release 203 Pages build."""
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
assert manifest['version'] == 203
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
manifest.update(version=204, landingGearRevision=204)
release = json.dumps(manifest) + '\n'
manifest_path.write_text(release)
Path('data/render-release.json').write_text(release)
subprocess.run([sys.executable, 'scripts/version-runtime.py'], check=True)
subprocess.run(['node','--test','tests/dreamliner-trucks203.test.mjs','tests/airframe-approach202.test.mjs'], cwd=dist, check=True)
changed = [*(dist / name for name in files), manifest_path]
names = {str(p.relative_to(dist)) for p in changed}
source = dist/'sources/game-source.zip'
tmp = source.with_suffix('.204.zip')
with zipfile.ZipFile(source) as old, zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED) as new:
    for item in old.infolist():
        if item.filename not in names:
            new.writestr(item, old.read(item.filename))
    for path in changed:
        new.write(path, str(path.relative_to(dist)))
tmp.replace(source)
