from pathlib import Path
import json,re,hashlib,gzip,base64,zipfile
root=Path('.');dist=root/'dist';b=json.loads(gzip.decompress(base64.b64decode(Path('source193.b64').read_text())));assert b['schema']==193
sha=lambda s:hashlib.sha256(s.encode()).hexdigest();pending={}
for name,patch in b['patches'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts
 s=re.sub(r'(?<=\.js)\?v=[0-9.]+','',(dist/p).read_text());assert sha(s)==patch['before'],'Unexpected release192 source: '+name
 for i,j,replacement in reversed(patch['ops']):s=s[:i]+replacement+s[j:]
 assert sha(s)==patch['after'],'Patched source hash mismatch: '+name
 pending[name]=s
for name,s in b['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;pending[name]=s
for name,s in pending.items():p=dist/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
p=dist/'data/render-release.json';d=json.loads(p.read_text());assert d['version']==192;d.update(version=193,aircraftSystemsRevision=193,approachMonitorRevision=193);p.write_text(json.dumps(d)+'\n');Path('data').mkdir(exist_ok=True);Path('data/render-release.json').write_text(p.read_text());pending['data/render-release.json']=''
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.193.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in pending:new.writestr(item,old.read(item.filename))
 for name in pending:new.write(dist/name,name)
tmp.replace(source);print('Applied systems and approach 193:',len(pending),'files; original aircraft assets unchanged')
