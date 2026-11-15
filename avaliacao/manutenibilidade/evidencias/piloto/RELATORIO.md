# Relatório dos pilotos — 08/11/2026

Produto no commit fixado `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`. Execução por Codex nesta sessão; não houve executor humano de M1.3. Todos os valores são do piloto, sem extrapolar para coleta formal.

## Execuções estáticas

| Métrica | Recorte | Numerador | Denominador | Valor (%) | Classificação |
|---|---|---|---|---|---|
| M1.2 | API | 1 | 137 | 0.7299 | Nota 3 |
| M1.2 | frontend | 0 | 213 | 0.0000 | Nota 3 |
| M1.2 | scraper | 0 | 18 | 0.0000 | Nota 3 |
| M1.2 | gerador | 0 | 15 | 0.0000 | Nota 3 |
| M1.1 | API | 2 | 50 | 4.0000 | Nota 2 |
| M1.1 | frontend | 3 | 60 | 5.0000 | Nota 2 |

Dados completos em `estatica/`: inventário com hashes/exclusões, grafos brutos e normalizados, blocos, JSON ESLint, CSV, versões e comandos com códigos de saída. Valores calculados sem arredondamento; a tabela arredonda só para exibição.

### Auditoria de M1.1

O pydeps por pacote omitiu 13 arquivos Python, incluindo módulos em diretórios sem `__init__.py`. Tentativas de análise individual e falhas de import relativo estão arquivadas em `comandos.json` e `pydeps-complementos.json`. Corrigiu-se o procedimento com leitura AST de todos os 50 arquivos; as arestas adicionais estão discriminadas por origem, destino e linha em `ciclos.json`. Não se usou ausência de nó como evidência de isolamento. Todos os 60 arquivos do frontend aparecem no Madge. Os warnings restantes são dependências externas, fora da métrica; aliases internos foram resolvidos com `baseUrl` absoluto em memória.

Imports dos ciclos conferidos nos fontes:

- API: `api/serializers.py:4` importa `utils.db_handler`; `utils/db_handler.py:2` importa `api.serializers`.
- Frontend: `SignInSection.tsx:5` importa `useUser`; `useUser.ts:4` importa `UserContext`; `UserContext.tsx:5` importa o tipo de `SignInSection`. Dependências de tipo integram o método.

O complemento AST resolve imports estáticos por módulos locais; imports construídos dinamicamente exigem inspeção adicional caso sejam introduzidos. Em novas versões, refazer a auditoria; o script gera notas candidatas até a conferência dos ciclos.

### Auditoria de M1.2

A conferência detectou métodos repetidos na saída do Radon: a extração foi corrigida para deduplicar por arquivo, linha e nome. A execução final verifica unicidade e confronta a regra ESLint nos limites 0 e 10. Sem erros fatais de parsing. Blocos fora de funções/métodos ficam em relatório separado.

Inspeção dos componentes críticos: `make_disciplines` (scraper, linha 200, CC 7) reúne desvios por tipo de linha HTML e construção dos campos. `_valid_schedule` (gerador, linha 153, CC 6) percorre horários e conflitos; `generate` (linha 209, CC 6) percorre combinações e decide as mensagens de retorno. A revisão confirmou os pontos de decisão; nenhum desses blocos excede 10. Máximos por recorte em `maximos-cc.json`.

## M1.3 — Não avaliado

Fichas C1/C2 e protocolo preparados. Responsáveis definidos: Lucas executará a coleta formal; Joaquim executará o piloto e revisará a coleta formal. A elegibilidade de Lucas foi confirmada pelo usuário. Em 12/11/2026, o usuário substituiu Kaleb por Joaquim no piloto, na revisão da coleta formal e na conferência da cobertura. Piloto humano não executado. A elegibilidade de Joaquim deve ser verificada antes da sessão: não ter especificado, ensaiado nem conhecido a localização das alterações. Experiência com Python/Django, familiaridade com o produto, disponibilidade e máquina de Joaquim ainda precisam ser registradas. Guia operacional em `../../tarefas/GUIA-PILOTO-JOAQUIM.md`. O Docker desta máquina já está operacional. Não há patch, tempo ou nota inventados. Não ensaiar as mudanças com a pessoa reservada para a coleta formal.

## M1.4 — Piloto executado com Docker

Execução em 08/11/2026, conduzida por Codex com autorização do usuário. Os 108 testes originais passaram (2,841 s); códigos da suíte e do script iguais a 0. A cópia do produto permaneceu no commit fixado, sem alterações rastreadas. Foram iniciados apenas API, PostgreSQL e Redis, suficientes para esta métrica; frontend não participa da cobertura Python.

| Recorte | Linhas cobertas | Linhas executáveis | Cobertura (%) | Nota do piloto |
|---|---|---|---|---|
| API | 1143 | 1396 | 81,8768 | 2 |
| scraper | 156 | 160 | 97,5000 | 3 |
| gerador | 140 | 141 | 99,2908 | 3 |

Evidências em `M1.4/execucao-docker/`: configuração efetiva e log, códigos de saída, `coverage.json`, HTML, comparação com as exclusões do CI, versões/imagens/mount da API em `ambiente.json`, auditoria do inventário e `resultados.csv`. A tentativa anterior sem Docker foi preservada na pasta superior para manter o histórico.

A auditoria confrontou os 50 arquivos Python do inventário com os 50 arquivos do JSON: nenhum ausente ou extra, zero linhas excluídas. `utils/json_pretty.py`, `api/admin.py` e `users/admin.py` integram o denominador. Sete arquivos com linhas executáveis e nenhuma linha coberta também foram incluídos, listados em `auditoria-inventario.json`. O resumo foi extraído por `resumir_cobertura.py`, sem arredondamento antes da classificação. Joaquim ainda deve conferir os resultados; este piloto não substitui a coleta formal da Fase 4.

## Pendências para encerrar #38

- [x] Roteiros, configurações e destinos das evidências preparados.
- [x] Pilotos M1.1 e M1.2 executados e auditados.
- [x] Configuração própria de coverage validada.
- [x] Níveis 0–3 mapeados por métrica nos roteiros.
- [x] Responsáveis definidos: Lucas (coleta formal, piloto M1.4 e armazenamento/versionamento das evidências) e Joaquim (piloto C1/C2, revisão da coleta formal e conferência da cobertura). Joaquim guarda as soluções do piloto C1/C2 até a sessão formal.
- [x] Elegibilidade de Lucas confirmada pelo usuário. Ordem C1 → C2; documentação e busca permitidas, sem IA nem ajuda de terceiros durante a medição.
- [ ] Verificar a elegibilidade de Joaquim antes do piloto: não ter especificado, ensaiado nem conhecido a localização das alterações.
- [ ] Registrar o perfil descritivo de experiência e familiaridade dos executores antes das sessões.
- [x] Disponibilizar Docker no ambiente de avaliação desta máquina; a máquina de Joaquim ainda precisa ser preparada.
- [ ] Executar piloto humano C1/C2 e arquivar fichas, patches e logs.
- [x] Executar piloto M1.4 e conferir todos os arquivos/denominadores dos três recortes por comparação automática com o inventário.
- [ ] Joaquim conferir as evidências de cobertura.

Questões para a reunião estão no final do README desta pasta. A issue permanece aberta; não foi atualizada remotamente.

## Verificação de prontidão — 08/11/2026

A dependência [#37](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/issues/37) foi consultada: encerrada como concluída em 05/11/2026, com os quatro itens marcados. A verificação local `docker ps` ainda informa que Docker não está disponível nesta distribuição WSL. Saída preservada em `M1.4/prontidao-docker.txt`. Essa verificação não executa a suíte nem produz cobertura. Os pilotos M1.3/M1.4 continuam pendentes de execução.

## Prontidão após habilitação do Ubuntu — 08/11/2026

Docker acessível; API, PostgreSQL e Redis iniciados. Piloto M1.4 executado e auditado conforme seção acima. A verificação anterior de indisponibilidade permanece como histórico. Para encerrar #38 faltam a sessão humana C1/C2 com evidências verificáveis e a conferência de Joaquim. Nenhuma sessão humana foi simulada.
