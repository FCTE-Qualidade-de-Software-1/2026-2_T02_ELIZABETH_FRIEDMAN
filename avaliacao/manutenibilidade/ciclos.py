"""Normaliza grafos por arquivo e enumera componentes fortemente conexos."""
import ast, json, sys
from pathlib import Path
out=Path(sys.argv[1]); root=Path(sys.argv[2]).resolve()
inv=json.loads((out/'inventario.json').read_text())['incluidos']
report={}
for layer in ['api','web']:
    nodes={f for f in inv if f.startswith(layer+'/')}
    graph={f:set() for f in nodes}; seen=set()
    if layer=='api':
        raws=[json.loads((out/f'pydeps-{pkg}.json').read_text()) for pkg in ['api','core','users','utils']]
        raws.extend(json.loads((out/'pydeps-complementos.json').read_text()).values())
        for raw in raws:
            names={k:str(Path(v['path']).relative_to(root)) for k,v in raw.items() if v.get('path') and Path(v['path']).is_relative_to(root)}
            for k,v in raw.items():
                source=names.get(k)
                if source not in nodes: continue
                seen.add(source)
                graph[source].update(names[t] for t in v.get('imports',[]) if names.get(t) in nodes)
    else:
        raw=json.loads((out/'madge.json').read_text())
        for k,targets in raw.items():
            source='web/'+k
            if source in nodes:
                seen.add(source); graph[source].update('web/'+t for t in targets if 'web/'+t in nodes)
    audit=[]
    if layer=='api':
        modules={}
        for f in nodes:
            parts=Path(f).relative_to('api').with_suffix('').parts
            name='.'.join(parts[:-1] if parts[-1]=='__init__' else parts)
            modules[name]=f
        for f in sorted(nodes):
            parts=list(Path(f).relative_to('api').with_suffix('').parts)
            package=parts[:-1]
            for n in ast.walk(ast.parse((root/f).read_text())):
                targets=[]
                if isinstance(n,ast.Import): targets=[a.name for a in n.names]
                elif isinstance(n,ast.ImportFrom):
                    prefix='.'.join(package[:len(package)-n.level+1]) if n.level else ''
                    module='.'.join(x for x in [prefix,n.module] if x)
                    targets=[module]+[module+'.'+a.name for a in n.names]
                for t in targets:
                    if t in modules:
                        dest=modules[t]
                        if dest not in graph[f]: audit.append({'origem':f,'destino':dest,'linha':n.lineno,'motivo':'aresta confirmada por AST; complemento ao pydeps'})
                        graph[f].add(dest)
            seen.add(f)
    def reachable(n):
        todo=list(graph[n]); reached=set()
        while todo:
            x=todo.pop()
            if x not in reached:
                reached.add(x); todo.extend(graph[x]-reached)
        return reached
    reach={n:reachable(n) for n in nodes}; components=[]; visited=set()
    for n in sorted(nodes):
        if n in visited: continue
        s={x for x in reach[n] if n in reach[x]}
        if s:
            components.append(sorted(s)); visited.update(s)
    cyc=set().union(*(set(c) for c in components)) if components else set()
    report[layer]={'inventario':len(nodes),'presentes_no_grafo':len(seen),'ausentes':sorted(nodes-seen),'componentes_ciclicos':components,'arquivos_em_ciclos':len(cyc),'percentual_preliminar':100*len(cyc)/len(nodes),'arestas':{k:sorted(v) for k,v in sorted(graph.items())},'complementos_ast':audit,'estado':'Grafo complementado por inspeção AST; ver parecer do piloto'}
(out/'ciclos.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:{x:v for x,v in r.items() if x!='arestas'} for k,r in report.items()},ensure_ascii=False,indent=2))
# Registrar os dois recortes, preservando M1.2. Auditoria dos ciclos é obrigatória.
import csv, datetime
csvpath=out/'resultados.csv'
with csvpath.open() as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=[r for r in reader if r['metrica']!='M1.1']
for layer,r in report.items():
    value=r['percentual_preliminar']
    rows.append(dict(zip(fields,['M1.1','API' if layer=='api' else 'frontend','3d399e745383b05e8e3b1a7c97ac0fdbf93a0360',datetime.date.today().isoformat(),'pydeps 3.0.1 + AST' if layer=='api' else 'Madge 8.0.0',r['arquivos_em_ciclos'],r['inventario'],value,'%', 'A conferir: auditoria', 'ciclos.json','Nota candidata '+str(0 if value>10 else 1 if value>5 else 2 if value>0 else 3)])))
with csvpath.open('w') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
