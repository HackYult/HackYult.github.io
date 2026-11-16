"""Apply release 190 to the verified release-189 build, preserving old assets."""
from pathlib import Path
import base64,gzip,json,hashlib,re,zipfile,shutil,subprocess,sys
root=Path('.');dist=root/'dist';source=json.loads(gzip.decompress(base64.b64decode(Path('source190.b64').read_text())))
canonical=lambda s:re.sub(r'(?<=\.js)\?v=[0-9.]+','',s)
changed=[]
for name,p in source['patches'].items():
 f=dist/name;text=canonical(f.read_text());assert hashlib.sha256(text.encode()).hexdigest()==p['before'],'Unexpected base source: '+name
 for i,j,value in reversed(p['ops']):text=text[:i]+value+text[j:]
 assert hashlib.sha256(text.encode()).hexdigest()==p['after'],'Patch mismatch: '+name
 f.write_text(text);changed.append(name)
for name,text in source['files'].items():
 p=Path(name);assert not p.is_absolute() and '..'not in p.parts
 f=dist/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text);changed.append(name)
raw=Path('worker-source190.glb');assert hashlib.sha256(raw.read_bytes()).hexdigest()=='b74fd05bb04cdfd2dad0a587dac828e269dc306ac07e57058712ef59871c6e12'
subprocess.run([sys.executable,str(dist/'scripts/prepare-worker190.py'),str(raw),str(dist/'assets/ground-open190/worker.glb')],check=True)
assert (dist/'assets/ground-open190/worker.glb').stat().st_size<12000000
with zipfile.ZipFile(dist/'sources/ground-source190.zip','w',compression=zipfile.ZIP_DEFLATED)as z:
 z.write(raw,'source/jordan-original.glb');z.write(dist/'scripts/prepare-worker190.py','prepare-worker190.py');z.write(dist/'assets/ground-open190/NOTICE.md','NOTICE.md')
p=dist/'data/render-release.json';d=json.loads(p.read_text());d.update(version=190,flightDeskRevision=190,groundCrewRevision=190);p.write_text(json.dumps(d)+'\n');Path('data').mkdir(exist_ok=True);Path('data/render-release.json').write_text(p.read_text());changed.append('data/render-release.json')
sourceZip=dist/'sources/game-source.zip';tmp=sourceZip.with_suffix('.190.zip');names=set(changed)
with zipfile.ZipFile(sourceZip)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in names:new.writestr(item,old.read(item.filename))
 for name in changed:new.write(dist/name,name)
tmp.replace(sourceZip)
print('Applied Flight Desk 190:',len(changed),'source files; original aircraft models untouched')
