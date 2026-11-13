"""Coleta estática; resultados de M1.1 exigem auditoria humana antes da pontuação."""
import argparse, csv, datetime, hashlib, json, os, platform, subprocess, sys
from pathlib import Path
from radon.complexity import cc_visit

SHA = '3d399e745383b05e8e3b1a7c97ac0fdbf93a0360'
p = argparse.ArgumentParser()
p.add_argument('produto', type=Path)
p.add_argument('saida', type=Path)
a = p.parse_args()
root, out = a.produto.resolve(), a.saida.resolve()
out.mkdir(parents=True, exist_ok=True)
def dump(name, value):
    (out / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
commands=[]
def run(args, cwd=root):
    r = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    commands.append({'comando':args,'diretorio':str(cwd),'codigo':r.returncode,'stderr':r.stderr})
    dump('comandos.json', commands)
    if r.returncode: raise RuntimeError(r.stderr)
    return r.stdout
assert run(['git','rev-parse','HEAD']).strip() == SHA, 'Commit divergente'
assert not run(['git','status','--porcelain','--untracked-files=no']).strip(), 'Produto modificado'
files=run(['git','ls-files']).splitlines()
included=[]; excluded=[]
for f in files:
    q=Path(f)
    eligible=(f.startswith(tuple('api/'+x+'/' for x in ['api','core','users','utils'])) and q.suffix=='.py') or (f.startswith('web/') and q.suffix in ['.ts','.tsx'])
    if not eligible: continue
    reason=next((x for x in ['tests','migrations','node_modules','.next','__pycache__'] if x in q.parts),None)
    if q.name.startswith(('test_','next-env.')) or f.endswith('.d.ts'): reason='teste ou declaração gerada'
    if reason: excluded.append({'arquivo':f,'motivo':reason})
    else: included.append(f)
dump('inventario.json',{'incluidos':included,'excluidos':excluded,'sha256':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in included}})
dump('ambiente.json',{'versao':SHA,'data':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'sistema':platform.platform(),'node':run(['node','--version']).strip()})
blocks=[]
block_keys=set()
def walk(blocks_in, file):
    for b in blocks_in:
        if hasattr(b,'methods'):
            walk(b.methods,file)
        else:
            key=(file,b.lineno,b.name)
            if key in block_keys: continue
            block_keys.add(key)
            blocks.append({'arquivo':file,'nome':b.name,'linha':b.lineno,'cc':b.complexity})
            walk(getattr(b,'closures',[]),file)
for f in included:
    if f.endswith('.py'): walk(cc_visit((root/f).read_text()),f)
dump('radon-blocos.json',blocks)
for pkg in ['api','core','users','utils']:
    raw=run([str(Path(sys.executable).parent/'pydeps'),'--no-config','--show-deps','--no-output','--max-bacon','0','--noise-level','100000',pkg],root/'api')
    dump('pydeps-'+pkg+'.json',json.loads(raw))
seen=set()
for pkg in ['api','core','users','utils']:
    for item in json.loads((out/('pydeps-'+pkg+'.json')).read_text()).values():
        if item.get('path'): seen.add(str(Path(item['path']).resolve()))
extra={}
for f in included:
    if f.endswith('.py') and str(root/f) not in seen:
        try:
            raw=run([str(Path(sys.executable).parent/'pydeps'),'--no-config','--show-deps','--no-output','--max-bacon','0','--noise-level','100000',str(root/f)],root/'api')
            extra[f]=json.loads(raw)
        except RuntimeError as e:
            extra[f]={'erro': {'mensagem':str(e)}}
dump('pydeps-complementos.json',extra)
run(['node',str(Path(__file__).with_name('coletar_frontend.cjs')),str(root),str(out),str(out/'inventario.json')])
js0=json.loads((out/'eslint-0.json').read_text()); js10=json.loads((out/'eslint-10.json').read_text())
for r in js0+js10:
    assert not any(m.get('fatal') or m.get('ruleId') is None for m in r['messages']), 'Falha de parsing'
jsblocks=[]; other=[]
for r in js0:
    for m in r['messages']:
        if m['ruleId']!='complexity': continue
        import re
        entry={'arquivo':str(Path(r['filePath']).relative_to(root)),'linha':m['line'],'nome':m['message'],'cc':int(re.search(r'complexity of (\d+)',m['message'])[1])}
        (jsblocks if m.get('nodeType') in ['FunctionDeclaration','FunctionExpression','ArrowFunctionExpression'] else other).append(entry)
assert sum(b['cc']>10 for b in jsblocks)==sum(m['ruleId']=='complexity' and m.get('nodeType') in ['FunctionDeclaration','FunctionExpression','ArrowFunctionExpression'] for r in js10 for m in r['messages'])
dump('eslint-blocos.json',jsblocks); dump('eslint-outros.json',other)
rows=[]
for scope, bs in [('API',blocks),('frontend',jsblocks),('scraper',[b for b in blocks if b['arquivo']=='api/utils/web_scraping.py']),('gerador',[b for b in blocks if b['arquivo']=='api/utils/schedule_generator.py'])]:
    n=sum(b['cc']>10 for b in bs); d=len(bs); v=100*n/d if d else None
    rows.append({'metrica':'M1.2','recorte':scope,'versao':SHA,'data':datetime.date.today().isoformat(),'ferramenta':'Radon 6.0.1' if scope!='frontend' else 'ESLint 8.57.1','numerador':n,'denominador':d,'valor':v,'unidade':'%','estado':'Medido' if d else 'Não calculável','evidencia':'radon-blocos.json' if scope!='frontend' else 'eslint-blocos.json','observacoes':'Nota '+str(0 if v>20 else 1 if v>10 else 2 if v>5 else 3) if d else ''})
with (out/'resultados.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('Coleta estática guardada em',out)
