"""Give every local browser module the same release identity."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1];out=root/'dist';version=str(json.loads((root/'data/render-release.json').read_text())['version'])
def browser_text(file):
 try:return file.read_text(encoding='utf-8')
 except UnicodeDecodeError:
  print('Preserving binary browser resource:',file.relative_to(out));return None
query=r'''(?:\?[^'"\s]*)?'''
pattern=re.compile(r'''((?:from\s*|import\s*\(?\s*)['"])((?:\.{1,2}/|/)[^'"\s?]+\.js)'''+query+r'''(['"])''')
for directory in ['src','vendor','data']:
 for file in (out/directory).rglob('*.js'):
  text=browser_text(file)
  if text is not None:file.write_text(pattern.sub(lambda m:m[1]+m[2]+'?v='+version+m[3],text))
for file in out.rglob('*.html'):
 text=browser_text(file)
 if text is None:continue
 text=pattern.sub(lambda m:m[1]+m[2]+'?v='+version+m[3],text)
 text=re.sub(r'''(src=['"](?:\./)?src/[^'"?]+\.js)'''+query+r'''(['"])''',lambda m:m[1]+'?v='+version+m[2],text)
 text=re.sub(r'''(href=['"](?:style|cockpit|flight-layout)\.css)'''+query+r'''(['"])''',lambda m:m[1]+'?v='+version+m[2],text);file.write_text(text)
for file in (out/'src').glob('*.js'):
 text=browser_text(file)
 if text is None:continue
 text=re.sub(r'''(/(?:data/airport-buildings\.json\.gz|data/taxi-layouts\.json\.gz|data/real-taxiways\.json\.gz|data/airports\.json|assets/geographic-models/catalog\.json|data/clean-imagery\.json))(?:\?v=\d+)?''',lambda m:m[1]+'?v='+version,text);file.write_text(text)
