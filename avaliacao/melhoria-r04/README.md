# Ação da #46: recuperar a seleção após recarga (M8–R04)

Implementa a prioridade 1 da Fase 4 / #45. O código do produto está no
[fork](https://github.com/LucasMF1/2023-2-SuaGradeUnB/tree/fix/r04-selection-draft),
commit [`54c781189868b7138fbeb8659622fd3540cafdcb`](https://github.com/LucasMF1/2023-2-SuaGradeUnB/commit/54c781189868b7138fbeb8659622fd3540cafdcb).
Os dados e as capturas estão em [RELATORIO.md](../../docs/avaliacao/dados/acao-r04/RELATORIO.md).

## Reprodução

Requer Node >= 20, npm, Git e Chromium do Playwright. Partindo da raiz deste
repositório, instale o roteiro e prepare dois checkouts:

```sh
npm --prefix avaliacao/melhoria-r04 ci
npm --prefix avaliacao/melhoria-r04 exec -- playwright install chromium
git clone https://github.com/LucasMF1/2023-2-SuaGradeUnB.git /tmp/r04-original
git -C /tmp/r04-original checkout 3d399e745383b05e8e3b1a7c97ac0fdbf93a0360
git clone https://github.com/LucasMF1/2023-2-SuaGradeUnB.git /tmp/r04-corrigido
git -C /tmp/r04-corrigido checkout 54c781189868b7138fbeb8659622fd3540cafdcb
git -C /tmp/r04-corrigido apply "$PWD/avaliacao/melhoria-r04/aviso-turma.patch"
npm --prefix /tmp/r04-original/web ci
npm --prefix /tmp/r04-corrigido/web ci
```

Inicie os servidores em dois terminais separados:

```sh
npm --prefix /tmp/r04-original/web run dev -- --hostname 127.0.0.1 --port 3045
```

```sh
npm --prefix /tmp/r04-corrigido/web run dev -- --hostname 127.0.0.1 --port 3046
```

Na raiz do repositório da avaliação, execute:

```sh
BASE_URL=http://127.0.0.1:3045 VARIANTE=antes FONTE=/tmp/r04-original EVIDENCIAS=/tmp/nova-coleta-r04 node avaliacao/melhoria-r04/verificar.cjs
BASE_URL=http://127.0.0.1:3046 VARIANTE=depois FONTE=/tmp/r04-corrigido EVIDENCIAS=/tmp/nova-coleta-r04 node avaliacao/melhoria-r04/verificar.cjs
```

Use um novo diretório em `EVIDENCIAS` para preservar a coleta já registrada.
O roteiro inicial também consta do fork em `web/tests/r04/`. O patch
`aviso-turma.patch` acrescenta o toast e a verificação da recuperação parcial.
`massa.json` é sintética;
as requisições são interceptadas pelo Playwright, sem login ou banco reais.
Os servidores Next podem precisar de acesso à internet para baixar as fontes
na primeira compilação. Não é necessário configurar a API para esta verificação.

Na modalidade `antes`, “passou” significa que a reprodução confirmou a **perda
da seleção**. Na modalidade `depois`, significa que a asserção da correção passou.
Qualquer asserção falha encerra o processo com código diferente de zero. Cada
contexto tem armazenamento inicialmente vazio; o celular é emulado pelo Chromium.

## Aplicar o patch sem usar o fork

`correcao.patch` é o commit completo, incluindo os testes. Em um checkout limpo
da origem `3d399e7`, execute:

```sh
git am /caminho/para/avaliacao/melhoria-r04/correcao.patch
git apply /caminho/para/avaliacao/melhoria-r04/aviso-turma.patch
```

## Teste manual com dados reais

`proxy-api.cjs` permite abrir as duas versões com as disciplinas reais do período.
Ele escuta em `127.0.0.1:8999`, repassa apenas GET para a API pública e bloqueia
login (401) e gravações (403), de modo que o site fica no modo anônimo.

```sh
node avaliacao/melhoria-r04/proxy-api.cjs
echo NEXT_PUBLIC_API_URL=http://127.0.0.1:8999 > /tmp/r04-original/web/.env.local
echo NEXT_PUBLIC_API_URL=http://127.0.0.1:8999 > /tmp/r04-corrigido/web/.env.local
```

Depois, suba os servidores nas portas 3045 e 3046 como acima e abra
`/schedules/home` nas duas. O teste de 21/11/2026 está registrado no
[relatório](../../docs/avaliacao/dados/acao-r04/RELATORIO.md#teste-manual-com-dados-reais-21112026).

## Escopo da entrega pelo fork

`web/tests/r04/` é material da avaliação e pode permanecer nesta entrega pelo
fork. Para um futuro PR ao projeto original, retirar essa pasta e preparar os
testes conforme as convenções do projeto, sem caminhos padrão para o repositório
da avaliação. O patch complementar inclui essa observação no README dos testes.
