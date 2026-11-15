# Auditoria dos ciclos de M1.1 (coleta formal, 15/11/2026)

Produto no commit `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`, sem alterações rastreadas.
Ferramentas: pydeps 3.0.1 e leitura AST (API), Madge 8.0.0 (frontend). Versões e máquina em
`ambiente.json`, `python-dependencias.txt` e `comandos.json`.

## Completude

- API: 50 arquivos Python no inventário, 50 presentes no grafo, nenhum ausente. As arestas
  que o pydeps não listou foram complementadas pela AST e estão em `ciclos.json`
  (`complementos_ast`), com origem, destino e linha.
- Frontend: 60 arquivos TS/TSX no inventário, todos presentes no Madge. Os avisos do Madge
  (`madge-warnings.json`) são só dependências externas (`react`, `next`, `axios` e similares),
  fora do grafo interno.

## Ciclos conferidos nos fontes

| Recorte | Componente cíclico | Imports que fecham o ciclo |
|---|---|---|
| API | `api/api/serializers.py` e `api/utils/db_handler.py` | `serializers.py` linha 4: `import utils.db_handler as dbh`; `db_handler.py` linha 2: `from api.serializers import ClassSerializerSchedule` |
| Frontend | `SignInSection.tsx`, `useUser.ts`, `UserContext.tsx` | `SignInSection.tsx` linha 5 importa `useUser`; `useUser.ts` linha 4 importa `UserContext`; `UserContext.tsx` linha 5 importa o tipo `UserData` de `SignInSection` |

No frontend, o ciclo inclui uma referência de tipo (`UserData`), como prevê o método
(dependências de tipo entram no grafo).

## Verificação independente da API

Foi escrita uma segunda análise, separada de `ciclos.py`: leitura AST dos 50 arquivos do
inventário, resolução dos módulos internos e componentes fortemente conexos (Tarjan). Ela
encontrou o mesmo único componente cíclico (2 arquivos, 4,0%). O resultado coincide com o do
piloto de 08/11/2026 nas seis linhas de `resultados.csv`, embora a máquina seja outra
(Python 3.13 e Node 22 aqui; Python 3.12 e Node 24 no piloto).

## Resultado e limites

| Recorte | Arquivos em ciclos | Inventário | Percentual | Nota |
|---|---|---|---|---|
| API | 2 | 50 | 4,0% | 2 |
| Frontend | 3 | 60 | 5,0% | 2 |

O percentual do frontend está no limite superior da faixa de nota 2 (mais de 0 até 5). Um
único arquivo a mais em ciclo levaria a nota 1. A ferramenta e esta auditoria não comprovam
boa arquitetura, apenas a ausência ou presença de dependências circulares entre arquivos.

## Quem executou

A coleta e a conferência foram executadas por Claude (IA), sob direção de Kaleb, que revisa
e responde pelos dados. A execução consta em `docs/uso-de-ia.md`. A revisão humana desta
auditoria ainda precisa ser registrada por Kaleb.
