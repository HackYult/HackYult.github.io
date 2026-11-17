from pathlib import Path
import json,gzip,base64,subprocess,sys,zipfile,hashlib,re
root=Path('.');dist=root/'dist';b=json.loads(gzip.decompress(base64.b64decode(Path('source196.b64').read_text())));assert b['schema']==196
manifest=json.loads((dist/'data/render-release.json').read_text());assert manifest['version']==195
pending={};sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
for name,patch in b['patches'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;s=re.sub(r'(?<=\.js)\?v=[0-9.]+','',(dist/p).read_text());assert sha(s)==patch['before'],name
 for i,j,replacement in reversed(patch['ops']):s=s[:i]+replacement+s[j:]
 assert sha(s)==patch['after'];pending[name]=s
for name,s in b['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;pending[name]=s
for name,s in pending.items():target=dist/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s)
subprocess.run([sys.executable,'scripts/import-open-terminal196.py','--archive',str((root/'sbgr-open196.tar.gz').resolve())],cwd=dist,check=True)
subprocess.run([sys.executable,'tests/open-terminal196.test.py'],cwd=dist,check=True)
manifest.update(version=196,terminalAssets=196,openTerminalRevision=196);text=json.dumps(manifest)+'\n';(dist/'data/render-release.json').write_text(text);Path('data/render-release.json').write_text(text);pending['data/render-release.json']=''
subprocess.run([sys.executable,'scripts/version-runtime.py'],check=True)
pending['assets/geographic-models/catalog.json']=''
for folder in ['assets/geographic-models/open196-SBGR-terminal','reports/release196']:
 for p in (dist/folder).rglob('*'):
  if p.is_file():pending[str(p.relative_to(dist))]=''
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.196.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in pending:new.writestr(item,old.read(item.filename))
 for name in pending:new.write(dist/name,name)
tmp.replace(source);print('Imported authored Guarulhos terminal / original bridges / night sheets:',len(pending),'files')
