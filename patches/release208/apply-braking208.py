"""Add rejected-takeoff braking and runway distance feedback to free flight."""
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
assert manifest['version'] == 207
import gzip, base64
files = json.loads(gzip.decompress(base64.b64decode('H4sIAAAAAAAC/7Vae3ObuBb/KmpmNuAtJoDBNnZIJm3T3U7TppO4091J/YcMwmaLwQtyHjfxd79HD7DAcbfdO3dn6oB0dHR0nr8j9vGgLMIjvFqZf5UHI3Rz4M6Gs4Hv9GdR3Ld7EfEdd9CL7SGJfS+K8MDx4tgZWs5g4NixRfzYtl171h/0+67r953+gYFubjzbQOzfQbJc5QVFj0lWUpymV+vsDj+8KvA3Um5QXORLpJlHBR/tzviwYw1BFG38NUsJRQWJC1Iu1HVAAJMHU9jH6TsG4j8HaA9p8MzOepSH3wy9E5zAFCXi6aGkZFny55uIrHBB1wUxcFEktzid8vE4TeYLelaWCazLqIlDmtwSY72KgMvnd51aLN8DsdjPXrFOTV2QT2EBN4EUoDLDjHi+ix3LGkQuKBhjJ/SIHWLbiiLPtr3Qt4d+3x3043AQDYnler7Vs2eDYYTtMHI9bgbLQJZiBCHoFfmLhJREExAlj2PFDHKiS8XM1hL8VLbfNxD/gVMh9CwzPTboIikNmoTfWudbLR7KJKzPZ8/8yCMzL5yFQ4dYvdhz3Kjfj3o+ibBrEcvru4QM4xnB4cy3Bq7lOAPie16Mw9AaWvx89oBJxAUKc7AzSnEWJdn8DVnCQ1CadFHklKbk2LQPD3V4z9fhIsrvsqen0sTckNcUz0kQBNrV5cXF5eeJ1jnVQXFmzzHMvmfY0xugXNOce+f06cnqjCw4WbWjUFq9YU0JHN3Dw9IsaP5pgUvCXBE2eXV19v7dx9+0U7vBhS+5In+vSUkDnBSzvMjIqTX6gOnCXOJ7EB088hscjXsQW22U5t2CkJQPgFhG4+yGKpch5PqikresE0JErBJaWcdzhm44c3uzme9bFrYGYR8P3NiLh1GvN4uHrkMG2I3dyPftOPSx7Ua27w961szyh7g34NZxhmAeZziUDoPQLL/Xtd/Oz640IzbnBBen2pvLLx/REbq4fP3+/I020j5/0gxwesP3OmNO/uns6j16dfVeM1oq0C4/Av3l27eaYcMCx7bkirPPk0ux4kZMaxeX8PMB+MPv2R/wezW51Jp2NXoNHsxM52hy/gHE4TYo8nUW6bHJqSdkuSIFZgnC9p3TU3vYeamhr2sLjv9aiuM3WF2zE/O14G50XcKypyft4+XVh7MLTeztt03C7FmGeEW6Iu90S760MlHsRU7P64UQ825/MItsL+oTt+/4xPOc2SAc9C0CRnEs3/d6Q9/tef7AgwTix0CGPRFAEDs2yxAoBBdF2pffz88vtFFB4GgZTP+zsaagZGkiOKZm5FnLVTuMQpqEU/yEUdjS/8US2/XXk7PJ5+8aYTptav/5ZMg0n63TFIiOjtBkQVCcEihT5QJDkkcY+Rb6RhEPzG65IiRCc8iSKM4LRIF6jpdEKxEcFS3ziJhfM3LPc7NIA2w8QC5IIt7Z2mvOJWCcf0WmZ7vwHxDUK+N1BmUoz/YmZFSVNhTRDnpkSSeJkV7Vm1rd6EUQMAkkDUKxmrxAAk0biwnhH/xlU7F70aDu7C4+u2LGHtf0ekTRCbI6HZWdOPZNSmJqoIJ5/RTWVqJW2fyC3JKiVBZAhkyW6yUfB/o6ayp8Ogq5qNtA2BISzl8naIV8BRUpVdnGJmPM3Rs9PbESC4zYJs2hbXrmQ52xoqs8+407MpuB8OLP16S4TUIihupKBa9C6wjpUvDDQ6Q3jnyCTNth64So7JW9VXprxGOntu+uBwTIGv8L2wuxakMiCI3f8zTiHl/SfIXWGU1S/rpK0pwiFlMlykF0s+IRmyJcjhWn33eEvQ6q+NgGkRRSGmPdUNVxgEzLZSp8xvhX52dv/tT28284h7KD8IwkazgcM4Pr7WcmNqs0uREoS+SeXTysJJ4Kzc1JPskv8hCnWwi3BVmMcUUpU5iAoPYA4LLY4VNeJix1wNCWhSTugu/TIk9hrsUNUsSPYMbdBCU2vSbzJcloqQPMYfOQl3JQWJJJTYmYKyUVKOpmynXEUqgu41esRHmMMnKHrgmtmW29W6Ev7hipJDk1hRwlc6+baU0vQ7O4M/GpyVzlQf+4Xs7ARZPybZIlFPwOVjCC2T6CDpOeJtmajCumjePAadq20Ldm1E3TZNvXCjHQzuRMmYTXuySiCyYWONpYPYfcEBJVNgcKlmhrnZqrdbnQH4GhHDEQAagxQjpwzKBCMYaa1oGITBOqa0daZ1Nx39SBL0FCxXTMXXif0a8Ah4KKsjmvR3KJUoyUjFilEcTcne/K+sAZAGPQnggB9nId5gVLWO+ymOn+oe0jYl9m99Z2lUkecZpncwOFRV5CLxrsxgSTVQxWp+fJji2DNGUxLYmXE0lWaRsmeEbAs1Ln7DtbEmGxI+Ts+IoQKyIpxVWxYQwgMy4IZsgedSsm1cBL5Llg2F9Qr2/BrD20Og1mpCjybUGE/MS5G4wQyPmLejRBfoJ63h7hSql0Qfhy55RHjVMqnMXCk2Brup0dVKNycmUchh6ZY44q/sxfb0T0iTOB1ACgp8JzDbQkFPDYCG3n0Kk01qhlrK4Y34zbns023ufVz10qrHBGUhay9C3H6/zxusJe4NuUGEj0nEZ1K9DIedAuwEGjPFzz0A0LApXwPCXsTdciQnGSlpowGNCaYQrcPrJ4hWoiIEQXzpRkpErepVYTJ1lGit8nHy4Y8XG5Xi5x8XAiDsDbT/Cn46Nq/DjFM5KenNXI4LgkKSR6hIsEd/lk8PVgO83A7NeDk+N8xdRzAgj/+Eg+V2MXl192xqBa746d/bEzBiVnO3YkRIEHIeTxCgHwxaJcwuiqHhGGFkPlEuzFGInuYIBe5WB8QJRrdm3AASVKopQgHFOACbhK1GC4NEV4BmBFgHsTBOC8hG651U28WoFL6qBoFWcKQXkEMhNAd19A+RNjuiZmNUjkFfh6huhme7QpI5Vp7Tu0gmIq/YTlzkYthYSHwwWJLnkVqd7eQjmvnic5X1kJD4k5XOBszgTUOyg4aabRGIZrl9c7vNsQQ9L19Uby5O6v80qq1zuIBxK9yyJyz5EYsxNDuTtIWYXFbeDcqXsJ2QvVW4NMDZT7/M419G2Qqkv3gOMWeyn/aYVHIeUo8JnHvZRMJJ1WB6fXhYpXRmboHLyr0Sf9vPbrI0dJiWcpbykra7RJRKSVN3CKqUrfssaLFy17sIGGRdQK8LyxWc/ZUF8H7XOLZ00hOzTQabnmpUO5I7At1jJXVwWfKhreizXr5IrZ8nuGZH80KHh60/Ss2ggbd2BSq1JLw+JNCSfknlUzsSEsEe1hLT/bo36B6V80RYVcKpMCh9eQ3hmcZNpTOXfQLk2ToiHUTczDnuasyeYFirmQwJe8Owb4OS/wapGEIl3woIM1ilBqNuHy5DXlNrXwCd4y1MOTnA/SXAHgSqJq9QpCUhC0hr9bgK0KUG0/VjcXW4+3G7NtVTxbYy9+rx+Sev/nYatcylIrFeasFzJX+fInN2M1JhB1wzteql5a0wnMIhxpCcEut+bOJOt0vc86w7eABlhgqh5Sz/P2VjTUAOfYa+1VAMJsTxDgMIQQKzBPPseoa3qKMfjRXgZbuc9LmiwhP0Wip28do9ru13rjI6R3Hf6u7tORB9SaBmDSS1zWdnDKHfuZSTG1xW08U2Y0n89TZkKRTccKoqtHqmabAsQrd9ttNmwun2u62YzsfTOAPCP2rvTGkFBJ0SAQI0clLZJQpXyEbjQsAGvUrbR5xO/hoYSn+bzVckOXKzElJPWVeGwtfL7zfy2u9WUxaC3ZfnFSlzQjz2gFQovFni931f2lbLmDxyTE+UibnF9PNCPFdGQZgLnhF9zilrsFPMu2fHQjoL7W6x/ZQ83AoxvLsKbGjP01rd7U4M3FyLM20019UwouFwaVTk1oCSMdByfYTCL21WU2GA44IKpLbQkesdI7CvqOg1rL1W2CwbgaElpLQBWbK7wuSRTEOC3JGCqgwIniq6AcVSDgQ8n4oqYhdPY18RGaalZwIDAJhQTDl4qh7VckV+HFPqoFfCWjkWDBtDyjElf+BR61lwDfx404B6OE/nCjRsRjbAAv/rluI+KCebQOvlsAxm1iYLogmYTIHA2L+2wKr6tVmpASlQClwUsg9PnN5zblcHxAcwDVMUQTTx8a/6CqqF+VJJDWYdqVV76B6Vcdvs4SbxJY4+TY8Szr8FAmnGMPhl6+7DAWEtOI6DPJ32ucNku3Ud31jVs0DaxgWJXRazmscVMEu6+IcPJTElS3if8gg70zz/dissnx/Bu/fudNDJnwlmZHbtPxxlKuBreGu4nz8sse4Qdpfic/Y4iLPqiC7E6o6pswAME0iWmXOUmUoyyXl+vMLdj3nB+0Mt8iAAmbBpfyNrS/X7c7lvue7iVqk1oS+4P/PLs/74Ye2p8fAp6OBt6URyy04pSPfyA4C1Q2Vm/gjf8vPllh8ToVPQQAeX/Myv+8g+IFS5wBmfy4sL275+ZnXAEVJKHsYiEFQAsCQIRkczwHxxH9dAGZHk75cw7h2Q2DDL2f9Ig90aZ8vglM90ejop17eo1Y/yl9yi/16MPZH3W4gEqz9AGxG1NItoDFuXZFIhWazfj3i4KEJLnl3xqzPOvyy0/IxbiAnu8ntWu1ak1v/MOHQWorHjxuxu28/MO6sVu6qXEvWuFbfvUFegeF3JWIJFByCvAt0AEr4gZK5lCoQBcU3ycMOxgMcXDF8QtJxkWiih3VwEK6CNptRquSTrcltXEIvlheIIoTbFHEYxWWI1qsiXEPyOY/o+7Aswx5azuyNrvOuttv8D06vHswAAtparbfSy16iBNWFxsRERGyOn92I/YZIK5Fs4fWRvIyJAxjGExep8IhNp1/ll2wvGcIreLFUPQPr6wVyPPav+NRHcjflWEj/j+LzX8BXJhgafomAAA=')))
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
manifest.update(version=208, flightControlRevision=208)
release = json.dumps(manifest) + '\n'
manifest_path.write_text(release)
Path('data/render-release.json').write_text(release)
subprocess.run([sys.executable, 'scripts/version-runtime.py'], check=True)
subprocess.run(['node','--test','tests/runway-brakes208.test.mjs','tests/nose-control207.test.mjs','tests/manual-axes206.test.mjs','tests/gear-view205.test.mjs','tests/dreamliner-trucks203.test.mjs','tests/airframe-approach202.test.mjs'], cwd=dist, check=True)
changed = [*(dist / name for name in files), manifest_path]
names = {str(p.relative_to(dist)) for p in changed}
source = dist/'sources/game-source.zip'
tmp = source.with_suffix('.208.zip')
with zipfile.ZipFile(source) as old, zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED) as new:
    for item in old.infolist():
        if item.filename not in names:
            new.writestr(item, old.read(item.filename))
    for path in changed:
        new.write(path, str(path.relative_to(dist)))
tmp.replace(source)
