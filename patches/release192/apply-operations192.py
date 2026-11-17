from pathlib import Path
import json,re,hashlib,gzip,base64,zipfile,subprocess,sys,shutil
root=Path('.');dist=root/'dist';b=json.loads(gzip.decompress(base64.b64decode(Path('source192.b64').read_text())));assert b['schema']==192
sha=lambda s:hashlib.sha256(s.encode()).hexdigest();pending={}
for name,patch in b['patches'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts
 s=re.sub(r'(?<=\.js)\?v=[0-9.]+','',(dist/p).read_text());assert sha(s)==patch['before'],'Unexpected release-191 source: '+name
 for i,j,replacement in reversed(patch['ops']):s=s[:i]+replacement+s[j:]
 assert sha(s)==patch['after'],'Patched source hash mismatch: '+name
 pending[name]=s
for name,s in b['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;pending[name]=s
for name,s in pending.items():p=dist/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
nav=Path('earth_nav192.dat');assert hashlib.sha256(nav.read_bytes()).hexdigest()=='1968bbe7bc24a189f15a6df2bfdff4b3502856bc8487f025b86c6cbfd81b0fae'
subprocess.run([sys.executable,str(dist/'scripts/build-ils192.py'),str(nav),str(dist/'data/airports.json'),str(dist/'data/ils192.json'),str(dist/'data/procedures136')],check=True);pending['data/ils192.json']=''
# Weather cache refresh failures retain the timestamped seed, never a false live report.
try:subprocess.run([sys.executable,str(dist/'scripts/weather-cache192.py'),'--airports',str(dist/'data/weather-airports192.json'),'--output',str(dist/'data/live-weather192.json')],check=True,timeout=100)
except(subprocess.SubprocessError,OSError):print('Live weather fetch unavailable; retaining bundled observation timestamps')
p=dist/'data/render-release.json';d=json.loads(p.read_text());d.update(version=192,operationsRevision=192,weatherCacheRevision=192);p.write_text(json.dumps(d)+'\n');Path('data').mkdir(exist_ok=True);Path('data/render-release.json').write_text(p.read_text());pending['data/render-release.json']=''
notice=(dist/'reports/release192/NOTICE.txt').read_text();attribution=dist/'ATTRIBUTION.md';previous=attribution.read_text()if attribution.exists()else''
attribution.write_text(previous+'\n\n## Release 192 navigation and weather\n\n'+notice);pending['ATTRIBUTION.md']=''
navarchive=dist/'sources/navigation-source192.zip';navarchive.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(navarchive,'w',compression=zipfile.ZIP_DEFLATED)as z:
 z.write(nav,'earth_nav.dat')
 for name,arc in [('scripts/build-ils192.py','build-ils192.py'),('reports/release192/LICENSE-GPL3.txt','LICENSE-GPL3.txt'),('reports/release192/NOTICE.txt','NOTICE.txt'),('data/ils192.json','ils192.json')]:z.write(dist/name,arc)
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.192.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in pending:new.writestr(item,old.read(item.filename))
 for name in pending:new.write(dist/name,name)
tmp.replace(source);print('Applied operations 192:',len(pending),'files; original model assets unchanged')
