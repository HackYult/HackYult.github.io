from pathlib import Path
import json,gzip,base64,subprocess,sys,zipfile,os
root=Path('.');dist=root/'dist';b=json.loads(gzip.decompress(base64.b64decode(Path('source198.b64').read_text())));assert b['schema']==198
manifest=json.loads((dist/'data/render-release.json').read_text());assert manifest['version']==197
pending={}
for name,s in b['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;target=dist/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s);pending[name]=''
args=[sys.executable,'scripts/import-open-pudong198.py']
if os.environ.get('AERONAUT_PUDONG_SOURCE'):args+=['--upstream',os.environ['AERONAUT_PUDONG_SOURCE']]
subprocess.run(args,cwd=dist,check=True);subprocess.run([sys.executable,'tests/open-pudong198.test.py'],cwd=dist,check=True)
manifest.update(version=198,terminalAssets=198,openTerminalRevision=198);text=json.dumps(manifest)+'\n';(dist/'data/render-release.json').write_text(text);Path('data/render-release.json').write_text(text);pending['data/render-release.json']=''
subprocess.run([sys.executable,'scripts/version-runtime.py'],check=True);pending['assets/geographic-models/catalog.json']=''
for folder in ['assets/geographic-models/zspd-open198','assets/geographic-models/open198-ZSPD1','assets/geographic-models/open198-ZSPD2','reports/release198']:
 for p in(dist/folder).rglob('*'):
  if p.is_file():pending[str(p.relative_to(dist))]=''
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.198.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in pending:new.writestr(item,old.read(item.filename))
 for name in pending:new.write(dist/name,name)
tmp.replace(source);print('Imported original Pudong T1/T2:',len(pending),'files; no new authored model geometry')
