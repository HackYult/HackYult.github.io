from pathlib import Path
import json,gzip,base64,subprocess,sys,zipfile
root=Path('.');dist=root/'dist';b=json.loads(gzip.decompress(base64.b64decode(Path('source195.b64').read_text())));assert b['schema']==195
manifest=json.loads((dist/'data/render-release.json').read_text());assert manifest['version']==194,'Expected release194 base'
pending={}
for name,s in b['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;target=dist/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s);pending[name]=''
subprocess.run([sys.executable,'scripts/import-open-terminals195.py','--archive',str((root/'omdb-open195.tar.gz').resolve())],cwd=dist,check=True)
subprocess.run([sys.executable,'tests/open-terminals195.test.py'],cwd=dist,check=True)
manifest.update(version=195,terminalAssets=195,openTerminalRevision=195);text=json.dumps(manifest)+'\n';(dist/'data/render-release.json').write_text(text);Path('data/render-release.json').write_text(text);pending['data/render-release.json']=''
subprocess.run([sys.executable,'scripts/version-runtime.py'],check=True)
pending['assets/geographic-models/catalog.json']=''
for folder in ['assets/geographic-models/omdb-open195','assets/geographic-models/open195-OMDB-A','assets/geographic-models/open195-OMDB-B','assets/geographic-models/open195-OMDB-C','reports/release195']:
 for p in (dist/folder).rglob('*'):
  if p.is_file():pending[str(p.relative_to(dist))]=''
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.195.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in pending:new.writestr(item,old.read(item.filename))
 for name in pending:new.write(dist/name,name)
tmp.replace(source);print('Imported original GPL terminal models with full sources:',len(pending),'files')
