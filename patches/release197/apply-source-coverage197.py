from pathlib import Path
import json,re,hashlib,gzip,base64,subprocess,sys,zipfile
root=Path('.');dist=root/'dist';bundle=json.loads(gzip.decompress(base64.b64decode(Path('source197.b64').read_text())));assert bundle['schema']==197
manifest=json.loads((dist/'data/render-release.json').read_text());assert manifest['version']==196
sha=lambda s:hashlib.sha256(s.encode()).hexdigest();pending={}
for name,patch in bundle['patches'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;s=re.sub(r'(?<=\.js)\?v=[0-9.]+','',(dist/p).read_text());assert sha(s)==patch['before'],name
 for i,j,replacement in reversed(patch['ops']):s=s[:i]+replacement+s[j:]
 assert sha(s)==patch['after'];pending[name]=s
for name,s in bundle['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;pending[name]=s
for name,s in pending.items():p=dist/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
manifest.update(version=197,sourceTerminalCoverageRevision=197);text=json.dumps(manifest)+'\n';(dist/'data/render-release.json').write_text(text);Path('data/render-release.json').write_text(text);pending['data/render-release.json']=''
subprocess.run([sys.executable,'scripts/version-runtime.py'],check=True)
subprocess.run(['node','scripts/audit-source-coverage197.mjs'],cwd=dist,check=True);pending['reports/release197/source-coverage.json']=''
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.197.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in pending:new.writestr(item,old.read(item.filename))
 for name in pending:new.write(dist/name,name)
tmp.replace(source);print('Applied source coverage197; original airport geometry and textures unchanged')
