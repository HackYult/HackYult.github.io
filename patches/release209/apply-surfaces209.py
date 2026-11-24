"""Refine terminal surfaces and runway touchdown deposits."""
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
assert manifest['version'] == 208
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
manifest.update(version=209, runwaySurfaceRevision=209, terminalFinishRevision=209)
release = json.dumps(manifest) + '\n'
manifest_path.write_text(release)
Path('data/render-release.json').write_text(release)
subprocess.run([sys.executable, 'scripts/version-runtime.py'], check=True)
subprocess.run(['node','--test','tests/source-terminal-finish199.test.js','tests/runway-brakes208.test.mjs','tests/nose-control207.test.mjs','tests/manual-axes206.test.mjs','tests/gear-view205.test.mjs','tests/dreamliner-trucks203.test.mjs','tests/airframe-approach202.test.mjs'], cwd=dist, check=True)
changed = [*(dist / name for name in files), manifest_path]
names = {str(p.relative_to(dist)) for p in changed}
source = dist/'sources/game-source.zip'
tmp = source.with_suffix('.209.zip')
with zipfile.ZipFile(source) as old, zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED) as new:
    for item in old.infolist():
        if item.filename not in names:
            new.writestr(item, old.read(item.filename))
    for path in changed:
        new.write(path, str(path.relative_to(dist)))
tmp.replace(source)
