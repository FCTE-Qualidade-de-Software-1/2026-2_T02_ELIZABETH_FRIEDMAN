# Roteiros de manutenibilidade — issue #38

Referência normativa do projeto: `docs/fase-2.md`, seções 3.4 e 4.1. Esta pasta implementa F3-C1 (procedimentos reproduzíveis) e F3-C8 (método e recursos por métrica). Piloto e coleta formal são separados. Não alterar o produto em produção.

## Preparação comum

Produto: SuaGradeUnB, commit `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`. Obter cópia conforme Fase 3, seção 2.1. Executar os comandos abaixo na raiz deste repositório. Substituir `/caminho/2023-2-SuaGradeUnB` pelo caminho absoluto da cópia limpa. Os scripts rejeitam SHA diferente e alterações rastreadas. Conferir também `git status --short` para detectar código novo não rastreado antes de medir.

```bash
python3 -m venv /tmp/manutenibilidade-f3
/tmp/manutenibilidade-f3/bin/pip install -r avaliacao/manutenibilidade/requirements.txt
cd avaliacao/manutenibilidade
npm ci
cd ../..
export NODE_PATH="$PWD/avaliacao/manutenibilidade/node_modules"
/tmp/manutenibilidade-f3/bin/python avaliacao/manutenibilidade/coletar.py /caminho/2023-2-SuaGradeUnB avaliacao/manutenibilidade/evidencias/piloto/estatica
/tmp/manutenibilidade-f3/bin/python avaliacao/manutenibilidade/ciclos.py avaliacao/manutenibilidade/evidencias/piloto/estatica /caminho/2023-2-SuaGradeUnB
```

Saída esperada: coleta concluída, JSON válidos e quatro linhas de M1.2 no CSV. `ciclos.py` imprime os dois recortes de M1.1. Em caso de erro de parsing ou falha das ferramentas, corrigir a condição e repetir em novo diretório; não pontuar uma saída parcial. Para a coleta formal, trocar `piloto` por `formal` e guardar nova evidência.

`inventario.json` contém os arquivos incluídos, hashes e exclusões justificadas. Escopo Python: quatro pacotes de produção; TS/TSX: frontend, sem testes, migrações e declarações. Não excluir arquivos por complexidade ou ausência de testes. `ambiente.json` registra versão e máquina; `comandos.json` guarda comandos, diretórios, códigos e stderr. Arquivar também as versões instaladas (`pip freeze`, `npm ls --depth=0`) junto de cada coleta em outra máquina.

## M1.1 — Ciclos de importação

Método: grafos de dependências por arquivo e componentes fortemente conexos. Esse método conta cada arquivo uma vez, mesmo em vários ciclos, e preserva os arquivos isolados no denominador.

1. `coletar.py` executa pydeps nos quatro pacotes, com distância ilimitada e sem poda por grau. Arquiva os quatro grafos brutos.
2. Tenta analisar individualmente os arquivos ausentes. O pydeps pode falhar com import relativo em módulos sem `__init__.py`; a falha fica em `comandos.json` e no relatório de complementos.
3. `ciclos.py` normaliza caminhos, remove nós externos/sintéticos e complementa os imports Python pela AST de **todos** os arquivos do inventário. As arestas adicionais ficam listadas com arquivo e linha. Esse recurso complementar é necessário pelo problema encontrado no piloto; não se presume que um arquivo ausente seja isolado.
4. Madge usa o `tsconfig.json` do produto, fixando `baseUrl` absoluto em memória para resolver `@/*`. Inclui dependências de tipo. Guardar `madge.json` e warnings. Qualquer import interno pendente invalida o recorte; dependências externas ficam fora do grafo interno.
5. Conferir os imports dos componentes cíclicos nos fontes. No piloto, foram conferidos o ciclo `api/serializers.py ↔ utils/db_handler.py` e `SignInSection → useUser → UserContext → SignInSection` (inclui referência de tipo).
6. Em `ciclos.json`, conferir inventário, arquivos presentes e arestas; calcular `100 × arquivos_em_ciclos / inventario`. Registrar duas linhas de resultado (API/frontend), com numerador, denominador e parecer de auditoria. Sem completude confirmada, deixar sem nota.

Saída esperada: dois grafos normalizados e listas auditáveis de ciclos; zero ciclos também é um resultado possível. A ferramenta sozinha não comprova boa arquitetura.

## M1.2 — Complexidade ciclomática

Método: percentual de funções/métodos com CC > 10. Menor percentual facilita localizar recortes a investigar; não mede compreensão humana diretamente.

1. `coletar.py` usa Radon `cc_visit`, contando funções, métodos e closures uma vez; médias de classes não entram no denominador.
2. O frontend usa ESLint com parser TypeScript, sem configuração herdada. A regra `complexity` com limite 0 enumera funções; limite 10 confere a contagem dos excedentes. A configuração exata está em `coletar_frontend.cjs`.
3. Erros de parsing interrompem a coleta. Mensagens de construções fora de funções/métodos ficam em `eslint-outros.json`, sem compor o denominador principal.
4. Conferir `radon-blocos.json`, `eslint-blocos.json` e os relatórios brutos. Calcular `100 × blocos_CC_maior_10 / blocos` em API, frontend, scraper e gerador.
5. Publicar os quatro recortes de `resultados.csv`. Inspecionar manualmente os blocos de maior CC no scraper e no gerador e registrar o maior valor/localização como diagnóstico, sem nota adicional.

## M1.3 — Mudanças controladas

Método: tempo de mudança validada por tarefa, com testes de aceitação e regressão. As fichas estão em `tarefas/C1.md` e `tarefas/C2.md`; nenhuma alteração no produto foi feita nesta entrega.

1. Nomear executor e revisor. O executor não pode ter especificado, ensaiado ou conhecido a localização das alterações. Registrar experiência, familiaridade, ferramentas de auxílio e ordem. O mesmo executor faz ambas as tarefas.
2. Preparar duas cópias limpas independentes da versão inicial. Como o compose fixa nomes de contêineres, executar uma cópia de cada vez, conferindo a origem dos mounts/imagens. Não apagar volumes de outros projetos.
3. Subir ambiente conforme seção 2 da Fase 3; PostgreSQL/Redis locais, sem SIGAA. Confirmar a suíte antes de iniciar:
   `docker exec -w /usr/src/api django-api python3 manage.py test`.
   Guardar log e código de saída. Falha inicial bloqueia o ensaio.
4. Entregar uma ficha e iniciar cronômetro monotônico. Leitura, edição, depuração e espera pelos testes integram o tempo. Rodar os testes novos e a mesma suíte completa; guardar comandos e logs.
5. Encerrar quando todos os critérios passarem ou aos 90 min. Calcular minutos apenas em caso de sucesso. O revisor confere patch, critérios e logs após a sessão, fora do tempo.
6. Guardar evidências conforme as fichas. Piloto das mesmas mudanças deve ser feito por outra pessoa, preservando executor não treinado para a coleta formal.

Saída esperada: duas fichas preenchidas, patches com testes, logs antes/depois e tempo válido ou motivo de insucesso/Não avaliado. Não atribuir tempo fictício. Lucas executará C1/C2 na coleta formal; Kaleb executará o piloto e revisará a coleta formal. A elegibilidade de Lucas e Kaleb para os respectivos papéis foi confirmada pelo usuário. Preservar Lucas de exposição à solução do piloto.

## M1.4 — Cobertura de linhas

Método: linhas executáveis cobertas / linhas executáveis de produção. A configuração própria inclui código nunca executado, reduzindo o risco de denominador artificialmente pequeno.

1. Usar cópia limpa, antes das mudanças C1/C2, com ambiente da Fase 3 pronto. Confirmar coverage.py 7.3.2.
2. Rodar na raiz deste repositório:

```bash
bash avaliacao/manutenibilidade/cobertura.sh /caminho/2023-2-SuaGradeUnB avaliacao/manutenibilidade/evidencias/piloto/M1.4
```

3. O script copia `configs/coverage.ini`, publica a configuração efetiva e executa a suíte original. `source` inclui `api`, `core`, `users`, `utils`; testes e migrações são omitidos. `exclude_lines` vazio impede exclusão por `pragma: no cover`. `include_namespace_packages = True` inclui também arquivos em diretórios sem `__init__.py`. `manage.py` está fora de `source`.
4. Guardar log, códigos de saída, JSON e HTML. Conferir os caminhos do JSON contra o inventário Python: incluir `utils/json_pretty.py`, `api/admin.py`, `users/admin.py` e arquivos não executados. Qualquer diferença precisa de explicação antes da pontuação.
5. Extrair `covered_lines` e `num_statements` do total da API e dos arquivos `utils/web_scraping.py` e `utils/schedule_generator.py`. Não usar linhas físicas. Gerar três linhas no CSV, com `100 × covered_lines / num_statements`.
6. `comparacao-omit-ci.json` aplica adicionalmente a lista omitida pelo CI sobre os mesmos dados. É somente comparação, sem substituir o resultado principal. Suíte reprovada: preservar parcial sem confirmar H1.4.

## Pontuação e validade

Aplicar valores sem arredondar antes da classificação. Os métodos distinguem todas as notas previstas na Fase 2:

| Métrica | 0 | 1 | 2 | 3 | Recortes obrigatórios |
|---|---|---|---|---|---|
| M1.1 (%) | >10 | >5 até 10 | >0 até 5 | 0 | API e frontend |
| M1.2 (%) | >20 | >10 até 20 | >5 até 10 | 0 até 5 | API, frontend, scraper, gerador |
| M1.3 (min) | Insucesso/regressão/prazo excedido | >60 até 90 | >30 até 60 | >0 até 30 | C1 e C2 |
| M1.4 (%) | <70 | 70 até <80 | 80 até <90 | 90 até 100 | API, scraper, gerador |

Denominador zero: Não calculável. Infraestrutura inválida, interrupção externa ou dado ausente: Não avaliado, sem nota. M1.3: desistência por dificuldade é insucesso; tempo nulo/negativo é inválido. Não compensar recortes ruins por média. O piloto verifica o método; resultados formais pertencem à Fase 4.

## Situação e decisões da equipe

Consultar `evidencias/piloto/RELATORIO.md`. A issue só pode ser encerrada após piloto humano de M1.3 e piloto completo de M1.4; as pendências não foram marcadas como realizadas.

Responsáveis definidos:

- Lucas: executor de C1/C2 na coleta formal, executor do piloto de cobertura M1.4 e responsável por guardar e versionar as evidências. As soluções do piloto de C1/C2 devem permanecer sob guarda de Kaleb até a sessão formal, preservando Lucas de treinamento prévio.
- Kaleb: executor do piloto de C1/C2, revisor independente da coleta formal e responsável por conferir as evidências e os denominadores da cobertura da API, scraper e gerador.

Condições das sessões: ordem C1 → C2; permitidas documentação e busca, sem IA nem ajuda de terceiros durante a medição. Registrar qualquer desvio. Cada tarefa parte de uma cópia independente. Essas condições valem para piloto e coleta formal.

Pendências de execução:

- Elegibilidade de Lucas e Kaleb confirmada pelo usuário; falta apenas registrar o perfil descritivo, sem presumir anos de experiência.
- Registrar uma descrição breve da experiência e familiaridade de cada executor antes de iniciar.
- Em qual máquina com Docker/PostgreSQL/Redis funcionarão os pilotos?
- Quando executar piloto e coleta formal e quem revisará os procedimentos corrigidos?
