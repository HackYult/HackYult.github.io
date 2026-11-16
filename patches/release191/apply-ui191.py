from pathlib import Path
import json,re,hashlib,gzip,base64,zipfile
root=Path('.');dist=root/'dist';bundle=json.loads(gzip.decompress(base64.b64decode(Path('source191.b64').read_text())));app=dist/'src/app.js';s=re.sub(r'(?<=\.js)\?v=[0-9.]+','',app.read_text());assert hashlib.sha256(s.encode()).hexdigest()==bundle['before'],'Unexpected release-190 app source';s="import {installInterface191} from './interface191.js';\n"+s.replace("installPanelLayers142($('viewport'));changeWeather(weather);","installPanelLayers142($('viewport'));installInterface191();changeWeather(weather);");assert hashlib.sha256(s.encode()).hexdigest()==bundle['after'];app.write_text(s)
changed=['src/app.js']
for name,text in bundle['files'].items():
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts;f=dist/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text);changed.append(name)
p=dist/'data/render-release.json';d=json.loads(p.read_text());d.update(version=191,interfaceRevision=191);p.write_text(json.dumps(d)+'\n');Path('data/render-release.json').write_text(p.read_text());changed.append('data/render-release.json')
source=dist/'sources/game-source.zip';tmp=source.with_suffix('.191.zip')
with zipfile.ZipFile(source)as old,zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED)as new:
 for item in old.infolist():
  if item.filename not in changed:new.writestr(item,old.read(item.filename))
 for name in changed:new.write(dist/name,name)
tmp.replace(source);print('Applied interface 191:',len(changed),'source files')
