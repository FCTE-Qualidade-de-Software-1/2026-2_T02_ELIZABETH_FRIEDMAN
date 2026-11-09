# Indicadores PSM/CID (coleta automática)

<!-- Página gerada por scripts/coletar_metricas_psm.py. Não edite à mão. -->

Última coleta: **05/11/2026**. Os valores são calculados a partir das issues, milestones e pull requests do repositório. A definição dos indicadores e as decisões de gestão estão em [Métricas PSM/CID](metricas.md). Cada tabela vem acompanhada de gráficos que mostram os itens medidos um a um (PR, issue ou integrante). Passe o mouse sobre um item para ver os dados dele.


## Desempenho dos processos

| Indicador | Valor | Detalhe |
|---|---|---|
| PRs revisados no prazo | 52,6% | 10 de 19 PRs mergeados aprovados antes do merge e em até 48 h |
| PRs aprovados antes do merge | 57,9% | 11 de 19 PRs mergeados |
| Retrabalho (issues) | 23,8% | 5 de 21 issues concluídas com a label correcao ou reabertas |
| Retrabalho (horas) | 29,3% | 22 h de 75 h reais registradas em issues concluídas |

### I1 e I2 — Tempo até a aprovação de cada PR

<figure class="grafico">
<div class="grafico-legenda"><span><i class="g-azul"></i>aprovado antes do merge, em até 48 h</span><span><i class="g-verde"></i>aprovado antes do merge, depois de 48 h</span><span><i class="g-laranja"></i>aprovado só depois do merge (× = sem aprovação)</span></div>
<div class="grafico-rolagem"><svg viewBox="0 0 720 270" role="img" aria-label="Horas até a primeira aprovação de cada PR mergeado">
<text class="g-titulo-eixo" x="44.0" y="12.0" text-anchor="start">horas entre a abertura e a 1ª aprovação</text>
<line class="g-base" x1="44.0" y1="242.0" x2="708.0" y2="242.0"/>
<text class="g-tick" x="38.0" y="246.0" text-anchor="end">0</text>
<line class="g-grade" x1="44.0" y1="199.6" x2="708.0" y2="199.6"/>
<text class="g-tick" x="38.0" y="203.6" text-anchor="end">25</text>
<line class="g-grade" x1="44.0" y1="157.2" x2="708.0" y2="157.2"/>
<text class="g-tick" x="38.0" y="161.2" text-anchor="end">50</text>
<line class="g-grade" x1="44.0" y1="114.8" x2="708.0" y2="114.8"/>
<text class="g-tick" x="38.0" y="118.8" text-anchor="end">75</text>
<line class="g-grade" x1="44.0" y1="72.4" x2="708.0" y2="72.4"/>
<text class="g-tick" x="38.0" y="76.4" text-anchor="end">100</text>
<line class="g-grade" x1="44.0" y1="30.0" x2="708.0" y2="30.0"/>
<text class="g-tick" x="38.0" y="34.0" text-anchor="end">125</text>
<g class="marca"><title>PR #14 — EduardoWaski
Aberto: 18/10 13:07
Mergeado: 18/10 13:31
1ª aprovação: 18/10 13:31 (0,4 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="44.0" y="30" width="34.9" height="212"/><path class="g-azul" d="M49.5,242.0V242.0Q49.5,240.0 51.5,240.0H71.5Q73.5,240.0 73.5,242.0V242.0Z"/></g>
<text class="g-tick" x="61.5" y="258.0" text-anchor="middle">#14</text>
<g class="marca"><title>PR #15 — EduardoWaski
Aberto: 18/10 13:10
Mergeado: 18/10 13:37
1ª aprovação: 18/10 13:37 (0,5 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="78.9" y="30" width="34.9" height="212"/><path class="g-azul" d="M84.4,242.0V242.0Q84.4,240.0 86.4,240.0H106.4Q108.4,240.0 108.4,242.0V242.0Z"/></g>
<text class="g-tick" x="96.4" y="258.0" text-anchor="middle">#15</text>
<g class="marca"><title>PR #16 — LucasMF1
Aberto: 18/10 20:32
Mergeado: 18/10 23:21
1ª aprovação: 21/10 19:25 (70,9 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="113.9" y="30" width="34.9" height="212"/><path class="g-laranja" d="M119.4,242.0V125.8Q119.4,121.8 123.4,121.8H139.4Q143.4,121.8 143.4,125.8V242.0Z"/></g>
<text class="g-tick" x="131.4" y="258.0" text-anchor="middle">#16</text>
<g class="marca"><title>PR #17 — JoaquimNetoo
Aberto: 18/10 22:54
Mergeado: 18/10 23:04
1ª aprovação: 21/10 19:25 (68,5 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="148.8" y="30" width="34.9" height="212"/><path class="g-laranja" d="M154.3,242.0V129.8Q154.3,125.8 158.3,125.8H174.3Q178.3,125.8 178.3,129.8V242.0Z"/></g>
<text class="g-tick" x="166.3" y="258.0" text-anchor="middle">#17</text>
<g class="marca"><title>PR #18 — JoaquimNetoo
Aberto: 18/10 22:56
Mergeado: 18/10 23:10
1ª aprovação: 21/10 19:26 (68,5 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="183.8" y="30" width="34.9" height="212"/><path class="g-laranja" d="M189.3,242.0V129.8Q189.3,125.8 193.3,125.8H209.3Q213.3,125.8 213.3,129.8V242.0Z"/></g>
<text class="g-tick" x="201.3" y="258.0" text-anchor="middle">#18</text>
<g class="marca"><title>PR #19 — JoaquimNetoo
Aberto: 19/10 00:04
Mergeado: 19/10 00:16
1ª aprovação: 21/10 19:28 (67,4 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="218.7" y="30" width="34.9" height="212"/><path class="g-laranja" d="M224.2,242.0V131.7Q224.2,127.7 228.2,127.7H244.2Q248.2,127.7 248.2,131.7V242.0Z"/></g>
<text class="g-tick" x="236.2" y="258.0" text-anchor="middle">#19</text>
<g class="marca"><title>PR #20 — camposs04
Aberto: 19/10 00:48
Mergeado: 19/10 00:53
1ª aprovação: 21/10 19:29 (66,7 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="253.7" y="30" width="34.9" height="212"/><path class="g-laranja" d="M259.2,242.0V132.9Q259.2,128.9 263.2,128.9H279.2Q283.2,128.9 283.2,132.9V242.0Z"/></g>
<text class="g-tick" x="271.2" y="258.0" text-anchor="middle">#20</text>
<g class="marca"><title>PR #21 — JoaquimNetoo
Aberto: 19/10 11:46
Mergeado: 19/10 11:46
1ª aprovação: 21/10 19:24 (55,6 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="288.6" y="30" width="34.9" height="212"/><path class="g-laranja" d="M294.1,242.0V151.6Q294.1,147.6 298.1,147.6H314.1Q318.1,147.6 318.1,151.6V242.0Z"/></g>
<text class="g-tick" x="306.1" y="258.0" text-anchor="middle">#21</text>
<g class="marca"><title>PR #22 — jpnunes2210
Aberto: 19/10 11:54
Mergeado: 19/10 12:35
1ª aprovação: 21/10 20:16 (56,4 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="323.6" y="30" width="34.9" height="212"/><path class="g-laranja" d="M329.1,242.0V150.4Q329.1,146.4 333.1,146.4H349.1Q353.1,146.4 353.1,150.4V242.0Z"/></g>
<text class="g-tick" x="341.1" y="258.0" text-anchor="middle">#22</text>
<g class="marca"><title>PR #23 — camposs04
Aberto: 19/10 12:33
Mergeado: 21/10 18:46
1ª aprovação: 21/10 19:20 (54,8 h após a abertura)
Aprovado só depois do merge</title><rect class="g-alvo" x="358.5" y="30" width="34.9" height="212"/><path class="g-laranja" d="M364.0,242.0V153.1Q364.0,149.1 368.0,149.1H384.0Q388.0,149.1 388.0,153.1V242.0Z"/></g>
<text class="g-tick" x="376.0" y="258.0" text-anchor="middle">#23</text>
<g class="marca"><title>PR #28 — JoaquimNetoo
Aberto: 21/10 21:17
Mergeado: 26/10 19:50
1ª aprovação: 26/10 19:49 (118,5 h após a abertura)
Aprovado antes do merge, depois de 48 h</title><rect class="g-alvo" x="393.5" y="30" width="34.9" height="212"/><path class="g-verde" d="M398.9,242.0V45.0Q398.9,41.0 402.9,41.0H418.9Q422.9,41.0 422.9,45.0V242.0Z"/></g>
<text class="g-tick" x="410.9" y="258.0" text-anchor="middle">#28</text>
<g class="marca"><title>PR #29 — jpnunes2210
Aberto: 26/10 14:22
Mergeado: 26/10 19:03
1ª aprovação: 26/10 19:03 (4,7 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="428.4" y="30" width="34.9" height="212"/><path class="g-azul" d="M433.9,242.0V238.1Q433.9,234.1 437.9,234.1H453.9Q457.9,234.1 457.9,238.1V242.0Z"/></g>
<text class="g-tick" x="445.9" y="258.0" text-anchor="middle">#29</text>
<g class="marca"><title>PR #31 — EduardoWaski
Aberto: 26/10 20:14
Mergeado: 26/10 21:02
1ª aprovação: 26/10 21:02 (0,8 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="463.4" y="30" width="34.9" height="212"/><path class="g-azul" d="M468.8,242.0V242.0Q468.8,240.0 470.8,240.0H490.8Q492.8,240.0 492.8,242.0V242.0Z"/></g>
<text class="g-tick" x="480.8" y="258.0" text-anchor="middle">#31</text>
<g class="marca"><title>PR #33 — JoaquimNetoo
Aberto: 26/10 22:01
Mergeado: 26/10 22:56
1ª aprovação: 26/10 22:55 (0,9 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="498.3" y="30" width="34.9" height="212"/><path class="g-azul" d="M503.8,242.0V242.0Q503.8,240.0 505.8,240.0H525.8Q527.8,240.0 527.8,242.0V242.0Z"/></g>
<text class="g-tick" x="515.8" y="258.0" text-anchor="middle">#33</text>
<g class="marca"><title>PR #34 — EduardoWaski
Aberto: 26/10 23:43
Mergeado: 26/10 23:45
1ª aprovação: 26/10 23:44 (0 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="533.3" y="30" width="34.9" height="212"/><path class="g-azul" d="M538.7,242.0V242.0Q538.7,240.0 540.7,240.0H560.7Q562.7,240.0 562.7,242.0V242.0Z"/></g>
<text class="g-tick" x="550.7" y="258.0" text-anchor="middle">#34</text>
<g class="marca"><title>PR #35 — JoaquimNetoo
Aberto: 28/10 15:21
Mergeado: 28/10 15:22
1ª aprovação: 28/10 15:22 (0 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="568.2" y="30" width="34.9" height="212"/><path class="g-azul" d="M573.7,242.0V242.0Q573.7,240.0 575.7,240.0H595.7Q597.7,240.0 597.7,242.0V242.0Z"/></g>
<text class="g-tick" x="585.7" y="258.0" text-anchor="middle">#35</text>
<g class="marca"><title>PR #53 — camposs04
Aberto: 03/11 18:20
Mergeado: 05/11 00:07
1ª aprovação: 05/11 00:07 (29,8 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="603.2" y="30" width="34.9" height="212"/><path class="g-azul" d="M608.6,242.0V195.5Q608.6,191.5 612.6,191.5H628.6Q632.6,191.5 632.6,195.5V242.0Z"/></g>
<text class="g-tick" x="620.6" y="258.0" text-anchor="middle">#53</text>
<g class="marca"><title>PR #56 — EduardoWaski
Aberto: 03/11 23:18
Mergeado: 04/11 00:15
1ª aprovação: 03/11 23:22 (0,1 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="638.1" y="30" width="34.9" height="212"/><path class="g-azul" d="M643.6,242.0V242.0Q643.6,240.0 645.6,240.0H665.6Q667.6,240.0 667.6,242.0V242.0Z"/></g>
<text class="g-tick" x="655.6" y="258.0" text-anchor="middle">#56</text>
<g class="marca"><title>PR #57 — EduardoWaski
Aberto: 05/11 00:47
Mergeado: 05/11 10:48
1ª aprovação: 05/11 10:47 (10 h após a abertura)
Aprovado antes do merge, em até 48 h</title><rect class="g-alvo" x="673.1" y="30" width="34.9" height="212"/><path class="g-azul" d="M678.5,242.0V229.0Q678.5,225.0 682.5,225.0H698.5Q702.5,225.0 702.5,229.0V242.0Z"/></g>
<text class="g-tick" x="690.5" y="258.0" text-anchor="middle">#57</text>
<line class="g-ref" x1="44.0" y1="160.6" x2="708.0" y2="160.6"/>
<text class="g-texto-ref" x="708.0" y="155.6" text-anchor="end">limite de 48 h</text>
</svg></div>
<figcaption>Cada coluna é um PR mergeado. A altura é o tempo entre a abertura e a primeira aprovação de outra pessoa. I1 conta só as colunas azuis, e I2 conta as azuis e as verdes. Passe o mouse sobre a coluna para ver as datas.</figcaption>
</figure>

### I3 e I4 — Horas de cada issue concluída e retrabalho

<figure class="grafico">
<div class="grafico-legenda"><span><i class="g-laranja"></i>retrabalho (label correcao ou reaberta)</span><span><i class="g-cinza"></i>demais issues concluídas (× = sem horas reais)</span></div>
<div class="grafico-rolagem"><svg viewBox="0 0 720 270" role="img" aria-label="Horas reais de cada issue concluída, com o retrabalho em destaque">
<text class="g-titulo-eixo" x="44.0" y="12.0" text-anchor="start">horas reais</text>
<line class="g-base" x1="44.0" y1="242.0" x2="708.0" y2="242.0"/>
<text class="g-tick" x="38.0" y="246.0" text-anchor="end">0</text>
<line class="g-grade" x1="44.0" y1="189.0" x2="708.0" y2="189.0"/>
<text class="g-tick" x="38.0" y="193.0" text-anchor="end">2</text>
<line class="g-grade" x1="44.0" y1="136.0" x2="708.0" y2="136.0"/>
<text class="g-tick" x="38.0" y="140.0" text-anchor="end">4</text>
<line class="g-grade" x1="44.0" y1="83.0" x2="708.0" y2="83.0"/>
<text class="g-tick" x="38.0" y="87.0" text-anchor="end">6</text>
<line class="g-grade" x1="44.0" y1="30.0" x2="708.0" y2="30.0"/>
<text class="g-tick" x="38.0" y="34.0" text-anchor="end">8</text>
<g class="marca"><title>#1 Fase 1 — Propósito da avaliação e partes interessadas
3 h reais</title><rect class="g-alvo" x="44.0" y="30" width="31.6" height="212"/><path class="g-cinza" d="M48.4,242.0V166.5Q48.4,162.5 52.4,162.5H67.2Q71.2,162.5 71.2,166.5V242.0Z"/></g>
<text class="g-tick" x="59.8" y="258.0" text-anchor="middle">#1</text>
<g class="marca"><title>#2 Fase 1 — Descrição do SuaGradeUnB e modelo de qualidade
6 h reais</title><rect class="g-alvo" x="75.6" y="30" width="31.6" height="212"/><path class="g-cinza" d="M80.0,242.0V87.0Q80.0,83.0 84.0,83.0H98.8Q102.8,83.0 102.8,87.0V242.0Z"/></g>
<g class="marca"><title>#3 Fase 1 — Priorização das características, escopo e ODS
6 h reais</title><rect class="g-alvo" x="107.2" y="30" width="31.6" height="212"/><path class="g-cinza" d="M111.7,242.0V87.0Q111.7,83.0 115.7,83.0H130.4Q134.4,83.0 134.4,87.0V242.0Z"/></g>
<text class="g-tick" x="123.0" y="258.0" text-anchor="middle">#3</text>
<g class="marca"><title>#4 Fase 2 — GQM de Usabilidade (Capacidade de interação)
4 h reais</title><rect class="g-alvo" x="138.9" y="30" width="31.6" height="212"/><path class="g-cinza" d="M143.3,242.0V140.0Q143.3,136.0 147.3,136.0H162.0Q166.0,136.0 166.0,140.0V242.0Z"/></g>
<g class="marca"><title>#5 Fase 2 — GQM de Eficiência de desempenho
3 h reais</title><rect class="g-alvo" x="170.5" y="30" width="31.6" height="212"/><path class="g-cinza" d="M174.9,242.0V166.5Q174.9,162.5 178.9,162.5H193.7Q197.7,162.5 197.7,166.5V242.0Z"/></g>
<text class="g-tick" x="186.3" y="258.0" text-anchor="middle">#5</text>
<g class="marca"><title>#6 Fase 2 — GQM de Manutenibilidade
3,5 h reais</title><rect class="g-alvo" x="202.1" y="30" width="31.6" height="212"/><path class="g-cinza" d="M206.5,242.0V153.2Q206.5,149.2 210.5,149.2H225.3Q229.3,149.2 229.3,153.2V242.0Z"/></g>
<g class="marca"><title>#7 Fase 2 — Critérios de julgamento, diagrama GQM e consistência com a Fase 1
4 h reais</title><rect class="g-alvo" x="233.7" y="30" width="31.6" height="212"/><path class="g-cinza" d="M238.1,242.0V140.0Q238.1,136.0 242.1,136.0H256.9Q260.9,136.0 260.9,140.0V242.0Z"/></g>
<text class="g-tick" x="249.5" y="258.0" text-anchor="middle">#7</text>
<g class="marca"><title>#8 Artigo — Template SBC e Metodologia
3 h reais</title><rect class="g-alvo" x="265.3" y="30" width="31.6" height="212"/><path class="g-cinza" d="M269.8,242.0V166.5Q269.8,162.5 273.8,162.5H288.5Q292.5,162.5 292.5,166.5V242.0Z"/></g>
<g class="marca"><title>#9 Artigo — Introdução e Referencial teórico
4 h reais</title><rect class="g-alvo" x="297.0" y="30" width="31.6" height="212"/><path class="g-cinza" d="M301.4,242.0V140.0Q301.4,136.0 305.4,136.0H320.1Q324.1,136.0 324.1,140.0V242.0Z"/></g>
<text class="g-tick" x="312.8" y="258.0" text-anchor="middle">#9</text>
<g class="marca"><title>#10 Artigo — Seções da Fase 1 e Fase 2 e revisão final
6 h reais</title><rect class="g-alvo" x="328.6" y="30" width="31.6" height="212"/><path class="g-cinza" d="M333.0,242.0V87.0Q333.0,83.0 337.0,83.0H351.8Q355.8,83.0 355.8,87.0V242.0Z"/></g>
<g class="marca"><title>#11 Gestão — Métricas PSM/CID e atas da E1
3 h reais</title><rect class="g-alvo" x="360.2" y="30" width="31.6" height="212"/><path class="g-cinza" d="M364.6,242.0V166.5Q364.6,162.5 368.6,162.5H383.4Q387.4,162.5 387.4,166.5V242.0Z"/></g>
<text class="g-tick" x="376.0" y="258.0" text-anchor="middle">#11</text>
<g class="marca"><title>#12 Fechamento da E1 — GitPage, contribuição e release
2,5 h reais</title><rect class="g-alvo" x="391.8" y="30" width="31.6" height="212"/><path class="g-cinza" d="M396.2,242.0V179.8Q396.2,175.8 400.2,175.8H415.0Q419.0,175.8 419.0,179.8V242.0Z"/></g>
<g class="marca"><title>#13 PC1 — Preparar material da apresentação
2,5 h reais</title><rect class="g-alvo" x="423.4" y="30" width="31.6" height="212"/><path class="g-cinza" d="M427.9,242.0V179.8Q427.9,175.8 431.9,175.8H446.6Q450.6,175.8 450.6,179.8V242.0Z"/></g>
<text class="g-tick" x="439.2" y="258.0" text-anchor="middle">#13</text>
<g class="marca"><title>#24 Artigo — Modelo SBC em coluna única e redução do conteúdo da E1
6 h reais
Retrabalho (reaberta)</title><rect class="g-alvo" x="455.0" y="30" width="31.6" height="212"/><path class="g-laranja" d="M459.5,242.0V87.0Q459.5,83.0 463.5,83.0H478.2Q482.2,83.0 482.2,87.0V242.0Z"/></g>
<g class="marca"><title>#25 Gestão — Métricas PSM/CID com dados reais e alinhadas ao modelo
5,5 h reais
Retrabalho (label correcao)</title><rect class="g-alvo" x="486.7" y="30" width="31.6" height="212"/><path class="g-laranja" d="M491.1,242.0V100.2Q491.1,96.2 495.1,96.2H509.9Q513.9,96.2 513.9,100.2V242.0Z"/></g>
<text class="g-tick" x="502.5" y="258.0" text-anchor="middle">#25</text>
<g class="marca"><title>#26 Gestão — Automatizar a coleta das métricas PSM/CID
8 h reais
Retrabalho (label correcao)</title><rect class="g-alvo" x="518.3" y="30" width="31.6" height="212"/><path class="g-laranja" d="M522.7,242.0V34.0Q522.7,30.0 526.7,30.0H541.5Q545.5,30.0 545.5,34.0V242.0Z"/></g>
<g class="marca"><title>#27 Gestão — Criar o GitHub Project do repositório
1,5 h reais
Retrabalho (label correcao)</title><rect class="g-alvo" x="549.9" y="30" width="31.6" height="212"/><path class="g-laranja" d="M554.3,242.0V206.2Q554.3,202.2 558.3,202.2H573.1Q577.1,202.2 577.1,206.2V242.0Z"/></g>
<text class="g-tick" x="565.7" y="258.0" text-anchor="middle">#27</text>
<g class="marca"><title>#30 Artigo — Atualizar a seção de PSM/CID com os indicadores da coleta automática
1 h reais
Retrabalho (label correcao)</title><rect class="g-alvo" x="581.5" y="30" width="31.6" height="212"/><path class="g-laranja" d="M586.0,242.0V219.5Q586.0,215.5 590.0,215.5H604.7Q608.7,215.5 608.7,219.5V242.0Z"/></g>
<g class="marca"><title>#32 Release da E1 — snapshot dos indicadores e publicação
1,5 h reais</title><rect class="g-alvo" x="613.1" y="30" width="31.6" height="212"/><path class="g-cinza" d="M617.6,242.0V206.2Q617.6,202.2 621.6,202.2H636.3Q640.3,202.2 640.3,206.2V242.0Z"/></g>
<text class="g-tick" x="629.0" y="258.0" text-anchor="middle">#32</text>
<g class="marca"><title>#37 Fase 3 — Ambiente de avaliação e massa de dados de referência
Sem horas reais registradas</title><rect class="g-alvo" x="644.8" y="30" width="31.6" height="212"/><path class="g-x g-cinza" d="M656.6,230.0l8,8m0,-8l-8,8"/></g>
<g class="marca"><title>#54 Gestão - Criar e adicionar a ata da reunião do dia 03/11
1 h reais</title><rect class="g-alvo" x="676.4" y="30" width="31.6" height="212"/><path class="g-cinza" d="M680.8,242.0V219.5Q680.8,215.5 684.8,215.5H699.6Q703.6,215.5 703.6,219.5V242.0Z"/></g>
<text class="g-tick" x="692.2" y="258.0" text-anchor="middle">#54</text>
</svg></div>
<figcaption>Cada coluna é uma issue concluída, com as horas reais registradas. I3 é a fração de colunas laranja, e I4 é a fração das horas que elas somam.</figcaption>
</figure>

## Calendário e progresso

| Indicador | Valor | Detalhe |
|---|---|---|
| Conclusão de issues — PC1 — Ponto de Controle 1 | 100,0% | 1 de 1 issues concluídas (prazo 19/10) |
| Conclusão de issues — E1 — Fases 1 e 2 | 100,0% | 18 de 18 issues concluídas (prazo 26/10) |
| Conclusão de issues — PC2 — Ponto de Controle 2 | 33,3% | 1 de 3 issues concluídas (prazo 16/11) |
| Conclusão de issues — E2 — Fases 3 e 4 | 6,7% | 1 de 15 issues concluídas (prazo 22/11) |
| Desvio de prazo médio | -5,1 dias | 1 de 21 issues concluídas depois do prazo do milestone (negativo = adiantado) |

### I5 — Issues de cada milestone

<figure class="grafico">
<div class="grafico-legenda"><span><i class="g-azul"></i>concluída</span><span><i class="g-aberta"></i>aberta</span></div>
<div class="grafico-rolagem"><svg viewBox="0 0 720 240" role="img" aria-label="Issues de cada milestone, concluídas e abertas">
<text class="g-rotulo" x="0.0" y="16.0" text-anchor="start">PC1 — Ponto de Controle 1</text>
<text class="g-tick" x="0.0" y="31.0" text-anchor="start">prazo 19/10</text>
<text class="g-valor" x="720.0" y="21.0" text-anchor="end">1 de 1 · 100%</text>
<g class="marca"><title>#13 PC1 — Preparar material da apresentação
Concluída em 19/10</title><rect class="g-chip-feita" x="176" y="4" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="189.0" y="21.0" text-anchor="middle">13</text></g>
<text class="g-rotulo" x="0.0" y="62.0" text-anchor="start">E1 — Fases 1 e 2</text>
<text class="g-tick" x="0.0" y="77.0" text-anchor="start">prazo 26/10</text>
<text class="g-valor" x="720.0" y="67.0" text-anchor="end">18 de 18 · 100%</text>
<g class="marca"><title>#1 Fase 1 — Propósito da avaliação e partes interessadas
Concluída em 16/10</title><rect class="g-chip-feita" x="176" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="189.0" y="67.0" text-anchor="middle">1</text></g>
<g class="marca"><title>#2 Fase 1 — Descrição do SuaGradeUnB e modelo de qualidade
Concluída em 18/10</title><rect class="g-chip-feita" x="206" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="219.0" y="67.0" text-anchor="middle">2</text></g>
<g class="marca"><title>#3 Fase 1 — Priorização das características, escopo e ODS
Concluída em 18/10</title><rect class="g-chip-feita" x="236" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="249.0" y="67.0" text-anchor="middle">3</text></g>
<g class="marca"><title>#4 Fase 2 — GQM de Usabilidade (Capacidade de interação)
Concluída em 18/10</title><rect class="g-chip-feita" x="266" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="279.0" y="67.0" text-anchor="middle">4</text></g>
<g class="marca"><title>#5 Fase 2 — GQM de Eficiência de desempenho
Concluída em 18/10</title><rect class="g-chip-feita" x="296" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="309.0" y="67.0" text-anchor="middle">5</text></g>
<g class="marca"><title>#6 Fase 2 — GQM de Manutenibilidade
Concluída em 18/10</title><rect class="g-chip-feita" x="326" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="339.0" y="67.0" text-anchor="middle">6</text></g>
<g class="marca"><title>#7 Fase 2 — Critérios de julgamento, diagrama GQM e consistência com a Fase 1
Concluída em 18/10</title><rect class="g-chip-feita" x="356" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="369.0" y="67.0" text-anchor="middle">7</text></g>
<g class="marca"><title>#8 Artigo — Template SBC e Metodologia
Concluída em 21/10</title><rect class="g-chip-feita" x="386" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="399.0" y="67.0" text-anchor="middle">8</text></g>
<g class="marca"><title>#9 Artigo — Introdução e Referencial teórico
Concluída em 21/10</title><rect class="g-chip-feita" x="416" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="429.0" y="67.0" text-anchor="middle">9</text></g>
<g class="marca"><title>#10 Artigo — Seções da Fase 1 e Fase 2 e revisão final
Concluída em 21/10</title><rect class="g-chip-feita" x="446" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="459.0" y="67.0" text-anchor="middle">10</text></g>
<g class="marca"><title>#11 Gestão — Métricas PSM/CID e atas da E1
Concluída em 18/10</title><rect class="g-chip-feita" x="476" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="489.0" y="67.0" text-anchor="middle">11</text></g>
<g class="marca"><title>#12 Fechamento da E1 — GitPage, contribuição e release
Concluída em 18/10</title><rect class="g-chip-feita" x="506" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="519.0" y="67.0" text-anchor="middle">12</text></g>
<g class="marca"><title>#24 Artigo — Modelo SBC em coluna única e redução do conteúdo da E1
Concluída em 26/10</title><rect class="g-chip-feita" x="536" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="549.0" y="67.0" text-anchor="middle">24</text></g>
<g class="marca"><title>#25 Gestão — Métricas PSM/CID com dados reais e alinhadas ao modelo
Concluída em 26/10</title><rect class="g-chip-feita" x="566" y="50" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="579.0" y="67.0" text-anchor="middle">25</text></g>
<g class="marca"><title>#26 Gestão — Automatizar a coleta das métricas PSM/CID
Concluída em 26/10</title><rect class="g-chip-feita" x="176" y="80" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="189.0" y="97.0" text-anchor="middle">26</text></g>
<g class="marca"><title>#27 Gestão — Criar o GitHub Project do repositório
Concluída em 05/11</title><rect class="g-chip-feita" x="206" y="80" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="219.0" y="97.0" text-anchor="middle">27</text></g>
<g class="marca"><title>#30 Artigo — Atualizar a seção de PSM/CID com os indicadores da coleta automática
Concluída em 26/10</title><rect class="g-chip-feita" x="236" y="80" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="249.0" y="97.0" text-anchor="middle">30</text></g>
<g class="marca"><title>#32 Release da E1 — snapshot dos indicadores e publicação
Concluída em 26/10</title><rect class="g-chip-feita" x="266" y="80" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="279.0" y="97.0" text-anchor="middle">32</text></g>
<text class="g-rotulo" x="0.0" y="134.0" text-anchor="start">PC2 — Ponto de Controle 2</text>
<text class="g-tick" x="0.0" y="149.0" text-anchor="start">prazo 16/11</text>
<text class="g-valor" x="720.0" y="139.0" text-anchor="end">1 de 3 · 33,3%</text>
<g class="marca"><title>#36 PC2 — Preparar material da apresentação
Aberta</title><rect class="g-chip-aberta" x="176" y="122" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="189.0" y="139.0" text-anchor="middle">36</text></g>
<g class="marca"><title>#54 Gestão - Criar e adicionar a ata da reunião do dia 03/11
Concluída em 04/11</title><rect class="g-chip-feita" x="206" y="122" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="219.0" y="139.0" text-anchor="middle">54</text></g>
<g class="marca"><title>#55 Gestão - Atualizar dados da gestão PSM/CID e elaborar gráficos de análise
Aberta</title><rect class="g-chip-aberta" x="236" y="122" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="249.0" y="139.0" text-anchor="middle">55</text></g>
<text class="g-rotulo" x="0.0" y="180.0" text-anchor="start">E2 — Fases 3 e 4</text>
<text class="g-tick" x="0.0" y="195.0" text-anchor="start">prazo 22/11</text>
<text class="g-valor" x="720.0" y="185.0" text-anchor="end">1 de 15 · 6,7%</text>
<g class="marca"><title>#37 Fase 3 — Ambiente de avaliação e massa de dados de referência
Concluída em 05/11</title><rect class="g-chip-feita" x="176" y="168" width="26" height="26" rx="4"/><text class="g-chip-feita-texto" x="189.0" y="185.0" text-anchor="middle">37</text></g>
<g class="marca"><title>#38 Fase 3 — Método e roteiros de Manutenibilidade (M1.1 a M1.4)
Aberta</title><rect class="g-chip-aberta" x="206" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="219.0" y="185.0" text-anchor="middle">38</text></g>
<g class="marca"><title>#39 Fase 3 — Método e roteiros de Eficiência de desempenho (M2 a M5)
Aberta</title><rect class="g-chip-aberta" x="236" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="249.0" y="185.0" text-anchor="middle">39</text></g>
<g class="marca"><title>#40 Fase 3 — Protocolo com participantes de Capacidade de interação (M6 a M9)
Aberta</title><rect class="g-chip-aberta" x="266" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="279.0" y="185.0" text-anchor="middle">40</text></g>
<g class="marca"><title>#41 Fase 3 — Cronograma da avaliação e consistência com a Fase 2
Aberta</title><rect class="g-chip-aberta" x="296" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="309.0" y="185.0" text-anchor="middle">41</text></g>
<g class="marca"><title>#42 Fase 4 — Coleta e análise de Manutenibilidade (G1)
Aberta</title><rect class="g-chip-aberta" x="326" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="339.0" y="185.0" text-anchor="middle">42</text></g>
<g class="marca"><title>#43 Fase 4 — Coleta e análise de Eficiência de desempenho (G2)
Aberta</title><rect class="g-chip-aberta" x="356" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="369.0" y="185.0" text-anchor="middle">43</text></g>
<g class="marca"><title>#44 Fase 4 — Sessões com participantes e análise de Capacidade de interação (G3)
Aberta</title><rect class="g-chip-aberta" x="386" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="399.0" y="185.0" text-anchor="middle">44</text></g>
<g class="marca"><title>#45 Fase 4 — Julgamento, relações entre as características e recomendações
Aberta</title><rect class="g-chip-aberta" x="416" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="429.0" y="185.0" text-anchor="middle">45</text></g>
<g class="marca"><title>#46 Fase 4 — Ação de melhoria
Aberta</title><rect class="g-chip-aberta" x="446" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="459.0" y="185.0" text-anchor="middle">46</text></g>
<g class="marca"><title>#47 Artigo — Metodologia atualizada, Resultados e Conclusão
Aberta</title><rect class="g-chip-aberta" x="476" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="489.0" y="185.0" text-anchor="middle">47</text></g>
<g class="marca"><title>#48 Artigo — Revisão final da 2ª versão
Aberta</title><rect class="g-chip-aberta" x="506" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="519.0" y="185.0" text-anchor="middle">48</text></g>
<g class="marca"><title>#50 Gestão — PSM/CID, atas e decisões da E2
Aberta</title><rect class="g-chip-aberta" x="536" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="549.0" y="185.0" text-anchor="middle">50</text></g>
<g class="marca"><title>#51 Fechamento da E2 — GitPage, contribuição e release
Aberta</title><rect class="g-chip-aberta" x="566" y="168" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="579.0" y="185.0" text-anchor="middle">51</text></g>
<g class="marca"><title>#52 Gestão - Preparar a apresentação da gestão PSM/CID
Aberta</title><rect class="g-chip-aberta" x="176" y="198" width="26" height="26" rx="4"/><text class="g-chip-aberta-texto" x="189.0" y="215.0" text-anchor="middle">52</text></g>
</svg></div>
<figcaption>Cada quadrado é uma issue do milestone, com o número dela. As descartadas ficam de fora. I5 é a fração de quadrados cheios.</figcaption>
</figure>

### I6 — Desvio de prazo de cada issue concluída

<figure class="grafico">
<div class="grafico-legenda"><span><i class="g-azul"></i>antes do prazo</span><span><i class="g-cinza"></i>no dia do prazo</span><span><i class="g-laranja"></i>depois do prazo</span></div>
<div class="grafico-rolagem"><svg viewBox="0 0 720 202" role="img" aria-label="Desvio de prazo de cada issue concluída, em dias">
<line class="g-ref" x1="446.0" y1="22.0" x2="446.0" y2="156.0"/>
<text class="g-texto-ref" x="446.0" y="16.0" text-anchor="middle">prazo do milestone</text>
<g class="marca"><title>#1 Fase 1 — Propósito da avaliação e partes interessadas
E1 — Fases 1 e 2, prazo 26/10
Fechada em 16/10, 10 dias antes do prazo</title><circle class="g-alvo" cx="200.3" cy="146.0" r="12.3"/><circle class="g-ponto g-azul" cx="200.3" cy="146.0" r="6"/></g>
<g class="marca"><title>#2 Fase 1 — Descrição do SuaGradeUnB e modelo de qualidade
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="146.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="146.0" r="6"/></g>
<g class="marca"><title>#3 Fase 1 — Priorização das características, escopo e ODS
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="131.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="131.0" r="6"/></g>
<g class="marca"><title>#4 Fase 2 — GQM de Usabilidade (Capacidade de interação)
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="116.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="116.0" r="6"/></g>
<g class="marca"><title>#5 Fase 2 — GQM de Eficiência de desempenho
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="101.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="101.0" r="6"/></g>
<g class="marca"><title>#6 Fase 2 — GQM de Manutenibilidade
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="86.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="86.0" r="6"/></g>
<g class="marca"><title>#7 Fase 2 — Critérios de julgamento, diagrama GQM e consistência com a Fase 1
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="71.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="71.0" r="6"/></g>
<g class="marca"><title>#11 Gestão — Métricas PSM/CID e atas da E1
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="56.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="56.0" r="6"/></g>
<g class="marca"><title>#12 Fechamento da E1 — GitPage, contribuição e release
E1 — Fases 1 e 2, prazo 26/10
Fechada em 18/10, 8 dias antes do prazo</title><circle class="g-alvo" cx="249.4" cy="41.0" r="12.3"/><circle class="g-ponto g-azul" cx="249.4" cy="41.0" r="6"/></g>
<g class="marca"><title>#8 Artigo — Template SBC e Metodologia
E1 — Fases 1 e 2, prazo 26/10
Fechada em 21/10, 5 dias antes do prazo</title><circle class="g-alvo" cx="323.1" cy="146.0" r="12.3"/><circle class="g-ponto g-azul" cx="323.1" cy="146.0" r="6"/></g>
<g class="marca"><title>#9 Artigo — Introdução e Referencial teórico
E1 — Fases 1 e 2, prazo 26/10
Fechada em 21/10, 5 dias antes do prazo</title><circle class="g-alvo" cx="323.1" cy="131.0" r="12.3"/><circle class="g-ponto g-azul" cx="323.1" cy="131.0" r="6"/></g>
<g class="marca"><title>#10 Artigo — Seções da Fase 1 e Fase 2 e revisão final
E1 — Fases 1 e 2, prazo 26/10
Fechada em 21/10, 5 dias antes do prazo</title><circle class="g-alvo" cx="323.1" cy="116.0" r="12.3"/><circle class="g-ponto g-azul" cx="323.1" cy="116.0" r="6"/></g>
<g class="marca"><title>#13 PC1 — Preparar material da apresentação
PC1 — Ponto de Controle 1, prazo 19/10
Fechada em 19/10, no dia do prazo</title><circle class="g-alvo" cx="446.0" cy="146.0" r="12.3"/><circle class="g-ponto g-cinza" cx="446.0" cy="146.0" r="6"/></g>
<g class="marca"><title>#24 Artigo — Modelo SBC em coluna única e redução do conteúdo da E1
E1 — Fases 1 e 2, prazo 26/10
Fechada em 26/10, no dia do prazo</title><circle class="g-alvo" cx="446.0" cy="131.0" r="12.3"/><circle class="g-ponto g-cinza" cx="446.0" cy="131.0" r="6"/></g>
<g class="marca"><title>#25 Gestão — Métricas PSM/CID com dados reais e alinhadas ao modelo
E1 — Fases 1 e 2, prazo 26/10
Fechada em 26/10, no dia do prazo</title><circle class="g-alvo" cx="446.0" cy="116.0" r="12.3"/><circle class="g-ponto g-cinza" cx="446.0" cy="116.0" r="6"/></g>
<g class="marca"><title>#26 Gestão — Automatizar a coleta das métricas PSM/CID
E1 — Fases 1 e 2, prazo 26/10
Fechada em 26/10, no dia do prazo</title><circle class="g-alvo" cx="446.0" cy="101.0" r="12.3"/><circle class="g-ponto g-cinza" cx="446.0" cy="101.0" r="6"/></g>
<g class="marca"><title>#30 Artigo — Atualizar a seção de PSM/CID com os indicadores da coleta automática
E1 — Fases 1 e 2, prazo 26/10
Fechada em 26/10, no dia do prazo</title><circle class="g-alvo" cx="446.0" cy="86.0" r="12.3"/><circle class="g-ponto g-cinza" cx="446.0" cy="86.0" r="6"/></g>
<g class="marca"><title>#32 Release da E1 — snapshot dos indicadores e publicação
E1 — Fases 1 e 2, prazo 26/10
Fechada em 26/10, no dia do prazo</title><circle class="g-alvo" cx="446.0" cy="71.0" r="12.3"/><circle class="g-ponto g-cinza" cx="446.0" cy="71.0" r="6"/></g>
<g class="marca"><title>#27 Gestão — Criar o GitHub Project do repositório
E1 — Fases 1 e 2, prazo 26/10
Fechada em 05/11, 10 dias depois do prazo</title><circle class="g-alvo" cx="691.7" cy="146.0" r="12.3"/><circle class="g-ponto g-laranja" cx="691.7" cy="146.0" r="6"/></g>
<g class="marca"><title>#37 Fase 3 — Ambiente de avaliação e massa de dados de referência
E2 — Fases 3 e 4, prazo 22/11
Fechada em 05/11, 17 dias antes do prazo</title><circle class="g-alvo" cx="28.3" cy="146.0" r="12.3"/><circle class="g-ponto g-azul" cx="28.3" cy="146.0" r="6"/></g>
<g class="marca"><title>#54 Gestão - Criar e adicionar a ata da reunião do dia 03/11
PC2 — Ponto de Controle 2, prazo 16/11
Fechada em 04/11, 12 dias antes do prazo</title><circle class="g-alvo" cx="151.1" cy="146.0" r="12.3"/><circle class="g-ponto g-azul" cx="151.1" cy="146.0" r="6"/></g>
<line class="g-base" x1="16.0" y1="156.0" x2="704.0" y2="156.0"/>
<text class="g-tick" x="28.3" y="172.0" text-anchor="middle">−17</text>
<text class="g-tick" x="52.9" y="172.0" text-anchor="middle">−16</text>
<text class="g-tick" x="77.4" y="172.0" text-anchor="middle">−15</text>
<text class="g-tick" x="102.0" y="172.0" text-anchor="middle">−14</text>
<text class="g-tick" x="126.6" y="172.0" text-anchor="middle">−13</text>
<text class="g-tick" x="151.1" y="172.0" text-anchor="middle">−12</text>
<text class="g-tick" x="175.7" y="172.0" text-anchor="middle">−11</text>
<text class="g-tick" x="200.3" y="172.0" text-anchor="middle">−10</text>
<text class="g-tick" x="224.9" y="172.0" text-anchor="middle">−9</text>
<text class="g-tick" x="249.4" y="172.0" text-anchor="middle">−8</text>
<text class="g-tick" x="274.0" y="172.0" text-anchor="middle">−7</text>
<text class="g-tick" x="298.6" y="172.0" text-anchor="middle">−6</text>
<text class="g-tick" x="323.1" y="172.0" text-anchor="middle">−5</text>
<text class="g-tick" x="347.7" y="172.0" text-anchor="middle">−4</text>
<text class="g-tick" x="372.3" y="172.0" text-anchor="middle">−3</text>
<text class="g-tick" x="396.9" y="172.0" text-anchor="middle">−2</text>
<text class="g-tick" x="421.4" y="172.0" text-anchor="middle">−1</text>
<text class="g-tick" x="446.0" y="172.0" text-anchor="middle">0</text>
<text class="g-tick" x="470.6" y="172.0" text-anchor="middle">+1</text>
<text class="g-tick" x="495.1" y="172.0" text-anchor="middle">+2</text>
<text class="g-tick" x="519.7" y="172.0" text-anchor="middle">+3</text>
<text class="g-tick" x="544.3" y="172.0" text-anchor="middle">+4</text>
<text class="g-tick" x="568.9" y="172.0" text-anchor="middle">+5</text>
<text class="g-tick" x="593.4" y="172.0" text-anchor="middle">+6</text>
<text class="g-tick" x="618.0" y="172.0" text-anchor="middle">+7</text>
<text class="g-tick" x="642.6" y="172.0" text-anchor="middle">+8</text>
<text class="g-tick" x="667.1" y="172.0" text-anchor="middle">+9</text>
<text class="g-tick" x="691.7" y="172.0" text-anchor="middle">+10</text>
<text class="g-titulo-eixo" x="360.0" y="192.0" text-anchor="middle">dias entre o fechamento da issue e o prazo do milestone</text>
</svg></div>
<figcaption>Cada ponto é uma issue concluída. Issues com o mesmo desvio ficam empilhadas. I6 é a média desses valores, e a média não mostra quantas issues fecharam no próprio dia do prazo.</figcaption>
</figure>

## Recursos e custos

| Indicador | Valor | Detalhe |
|---|---|---|
| Esforço real / estimado | 0,92 | 75 h reais / 81.5 h estimadas em 20 issues com os dois registros |
| Issues concluídas sem horas reais | 1 issues | de 21 issues concluídas |
| Distribuição de esforço — Eduardo Waski | 36,7% | 27.5 h de 75 h registradas |
| Distribuição de esforço — Joaquim Neto | 20,0% | 15 h de 75 h registradas |
| Distribuição de esforço — João Paulo Nunes | 13,3% | 10 h de 75 h registradas |
| Distribuição de esforço — Júlia Santana Campos | 10,7% | 8 h de 75 h registradas |
| Distribuição de esforço — LucasMF | 9,3% | 7 h de 75 h registradas |
| Distribuição de esforço — kalebmacedo | 10,0% | 7.5 h de 75 h registradas |

### I7 — Horas reais de cada integrante

<figure class="grafico">
<div class="grafico-rolagem"><svg viewBox="0 0 720 234" role="img" aria-label="Horas reais registradas por integrante">
<line class="g-base" x1="168.0" y1="24.0" x2="168.0" y2="208.0"/>
<text class="g-tick" x="168.0" y="224.0" text-anchor="middle">0</text>
<line class="g-grade" x1="314.7" y1="24.0" x2="314.7" y2="208.0"/>
<text class="g-tick" x="314.7" y="224.0" text-anchor="middle">10</text>
<line class="g-grade" x1="461.3" y1="24.0" x2="461.3" y2="208.0"/>
<text class="g-tick" x="461.3" y="224.0" text-anchor="middle">20</text>
<line class="g-grade" x1="608.0" y1="24.0" x2="608.0" y2="208.0"/>
<text class="g-tick" x="608.0" y="224.0" text-anchor="middle">30</text>
<line class="g-ref" x1="351.3" y1="20.0" x2="351.3" y2="208.0"/>
<text class="g-texto-ref" x="351.3" y="15.0" text-anchor="middle">média 12,5 h</text>
<g class="marca"><title>Eduardo Waski: 27,5 h em 11 registros, 36,7% do total</title><rect class="g-alvo" x="0" y="29.0" width="720" height="28"/><text class="g-rotulo" x="158.0" y="47.0" text-anchor="end">Eduardo Waski</text><path class="g-azul" d="M168.0,35.0H567.3Q571.3,35.0 571.3,39.0V47.0Q571.3,51.0 567.3,51.0H168.0Z"/><text class="g-valor" x="579.3" y="47.0" text-anchor="start">27,5 h · 36,7%</text></g>
<g class="marca"><title>Joaquim Neto: 15 h em 5 registros, 20% do total</title><rect class="g-alvo" x="0" y="59.0" width="720" height="28"/><text class="g-rotulo" x="158.0" y="77.0" text-anchor="end">Joaquim Neto</text><path class="g-azul" d="M168.0,65.0H384.0Q388.0,65.0 388.0,69.0V77.0Q388.0,81.0 384.0,81.0H168.0Z"/><text class="g-valor" x="396.0" y="77.0" text-anchor="start">15 h · 20%</text></g>
<g class="marca"><title>João Paulo Nunes: 10 h em 3 registros, 13,3% do total</title><rect class="g-alvo" x="0" y="89.0" width="720" height="28"/><text class="g-rotulo" x="158.0" y="107.0" text-anchor="end">João Paulo Nunes</text><path class="g-azul" d="M168.0,95.0H310.7Q314.7,95.0 314.7,99.0V107.0Q314.7,111.0 310.7,111.0H168.0Z"/><text class="g-valor" x="322.7" y="107.0" text-anchor="start">10 h · 13,3%</text></g>
<g class="marca"><title>Júlia Santana Campos: 8 h em 3 registros, 10,7% do total</title><rect class="g-alvo" x="0" y="119.0" width="720" height="28"/><text class="g-rotulo" x="158.0" y="137.0" text-anchor="end">Júlia Santana Campos</text><path class="g-azul" d="M168.0,125.0H281.3Q285.3,125.0 285.3,129.0V137.0Q285.3,141.0 281.3,141.0H168.0Z"/><text class="g-valor" x="293.3" y="137.0" text-anchor="start">8 h · 10,7%</text></g>
<g class="marca"><title>kalebmacedo: 7,5 h em 2 registros, 10% do total</title><rect class="g-alvo" x="0" y="149.0" width="720" height="28"/><text class="g-rotulo" x="158.0" y="167.0" text-anchor="end">kalebmacedo</text><path class="g-azul" d="M168.0,155.0H274.0Q278.0,155.0 278.0,159.0V167.0Q278.0,171.0 274.0,171.0H168.0Z"/><text class="g-valor" x="286.0" y="167.0" text-anchor="start">7,5 h · 10%</text></g>
<g class="marca"><title>LucasMF: 7 h em 2 registros, 9,3% do total</title><rect class="g-alvo" x="0" y="179.0" width="720" height="28"/><text class="g-rotulo" x="158.0" y="197.0" text-anchor="end">LucasMF</text><path class="g-azul" d="M168.0,185.0H266.7Q270.7,185.0 270.7,189.0V197.0Q270.7,201.0 266.7,201.0H168.0Z"/><text class="g-valor" x="278.7" y="197.0" text-anchor="start">7 h · 9,3%</text></g>
</svg></div>
<figcaption>Cada barra é a soma das horas reais que o integrante registrou nas issues, com a participação no total. A linha tracejada é a média do grupo.</figcaption>
</figure>

### I8 — Horas estimadas e reais de cada issue concluída

<figure class="grafico">
<div class="grafico-rolagem"><svg viewBox="0 0 460 400" role="img" aria-label="Horas estimadas e reais de cada issue concluída" style="max-width:460px">
<line class="g-base" x1="52.0" y1="16.0" x2="52.0" y2="354.0"/>
<line class="g-base" x1="52.0" y1="354.0" x2="444.0" y2="354.0"/>
<text class="g-tick" x="52.0" y="370.0" text-anchor="middle">0</text>
<text class="g-tick" x="46.0" y="358.0" text-anchor="end">0</text>
<line class="g-grade" x1="130.4" y1="16.0" x2="130.4" y2="354.0"/>
<line class="g-grade" x1="52.0" y1="286.4" x2="444.0" y2="286.4"/>
<text class="g-tick" x="130.4" y="370.0" text-anchor="middle">2</text>
<text class="g-tick" x="46.0" y="290.4" text-anchor="end">2</text>
<line class="g-grade" x1="208.8" y1="16.0" x2="208.8" y2="354.0"/>
<line class="g-grade" x1="52.0" y1="218.8" x2="444.0" y2="218.8"/>
<text class="g-tick" x="208.8" y="370.0" text-anchor="middle">4</text>
<text class="g-tick" x="46.0" y="222.8" text-anchor="end">4</text>
<line class="g-grade" x1="287.2" y1="16.0" x2="287.2" y2="354.0"/>
<line class="g-grade" x1="52.0" y1="151.2" x2="444.0" y2="151.2"/>
<text class="g-tick" x="287.2" y="370.0" text-anchor="middle">6</text>
<text class="g-tick" x="46.0" y="155.2" text-anchor="end">6</text>
<line class="g-grade" x1="365.6" y1="16.0" x2="365.6" y2="354.0"/>
<line class="g-grade" x1="52.0" y1="83.6" x2="444.0" y2="83.6"/>
<text class="g-tick" x="365.6" y="370.0" text-anchor="middle">8</text>
<text class="g-tick" x="46.0" y="87.6" text-anchor="end">8</text>
<line class="g-grade" x1="444.0" y1="16.0" x2="444.0" y2="354.0"/>
<line class="g-grade" x1="52.0" y1="16.0" x2="444.0" y2="16.0"/>
<text class="g-tick" x="444.0" y="370.0" text-anchor="middle">10</text>
<text class="g-tick" x="46.0" y="20.0" text-anchor="end">10</text>
<line class="g-ref" x1="52.0" y1="354.0" x2="444.0" y2="16.0"/>
<text class="g-texto-ref" x="373.6" y="97.6" text-anchor="start">real = estimado</text>
<text class="g-dica-canto" x="60.0" y="30.0" text-anchor="start">acima da linha: levou mais que o estimado</text>
<text class="g-dica-canto" x="436.0" y="346.0" text-anchor="end">abaixo: levou menos</text>
<g class="marca"><title>#30 Artigo — Atualizar a seção de PSM/CID com os indicadores da coleta automática: 1 h estimadas, 1 h reais
#54 Gestão - Criar e adicionar a ata da reunião do dia 03/11: 1 h estimadas, 1 h reais</title><circle class="g-alvo" cx="91.2" cy="320.2" r="12"/><circle class="g-ponto g-azul" cx="91.2" cy="320.2" r="5"/><text class="g-valor" x="100.2" y="314.2" text-anchor="start">×2</text></g>
<g class="marca"><title>#32 Release da E1 — snapshot dos indicadores e publicação: 1,5 h estimadas, 1,5 h reais</title><circle class="g-alvo" cx="110.8" cy="303.3" r="12"/><circle class="g-ponto g-azul" cx="110.8" cy="303.3" r="5"/></g>
<g class="marca"><title>#27 Gestão — Criar o GitHub Project do repositório: 2 h estimadas, 1,5 h reais</title><circle class="g-alvo" cx="130.4" cy="303.3" r="12"/><circle class="g-ponto g-azul" cx="130.4" cy="303.3" r="5"/></g>
<g class="marca"><title>#12 Fechamento da E1 — GitPage, contribuição e release: 3 h estimadas, 2,5 h reais</title><circle class="g-alvo" cx="169.6" cy="269.5" r="12"/><circle class="g-ponto g-azul" cx="169.6" cy="269.5" r="5"/></g>
<g class="marca"><title>#5 Fase 2 — GQM de Eficiência de desempenho: 3 h estimadas, 3 h reais
#11 Gestão — Métricas PSM/CID e atas da E1: 3 h estimadas, 3 h reais</title><circle class="g-alvo" cx="169.6" cy="252.6" r="12"/><circle class="g-ponto g-azul" cx="169.6" cy="252.6" r="5"/><text class="g-valor" x="178.6" y="246.6" text-anchor="start">×2</text></g>
<g class="marca"><title>#6 Fase 2 — GQM de Manutenibilidade: 3 h estimadas, 3,5 h reais</title><circle class="g-alvo" cx="169.6" cy="235.7" r="12"/><circle class="g-ponto g-azul" cx="169.6" cy="235.7" r="5"/></g>
<g class="marca"><title>#4 Fase 2 — GQM de Usabilidade (Capacidade de interação): 3 h estimadas, 4 h reais</title><circle class="g-alvo" cx="169.6" cy="218.8" r="12"/><circle class="g-ponto g-azul" cx="169.6" cy="218.8" r="5"/></g>
<g class="marca"><title>#13 PC1 — Preparar material da apresentação: 4 h estimadas, 2,5 h reais</title><circle class="g-alvo" cx="208.8" cy="269.5" r="12"/><circle class="g-ponto g-azul" cx="208.8" cy="269.5" r="5"/></g>
<g class="marca"><title>#1 Fase 1 — Propósito da avaliação e partes interessadas: 4 h estimadas, 3 h reais
#8 Artigo — Template SBC e Metodologia: 4 h estimadas, 3 h reais</title><circle class="g-alvo" cx="208.8" cy="252.6" r="12"/><circle class="g-ponto g-azul" cx="208.8" cy="252.6" r="5"/><text class="g-valor" x="217.8" y="246.6" text-anchor="start">×2</text></g>
<g class="marca"><title>#7 Fase 2 — Critérios de julgamento, diagrama GQM e consistência com a Fase 1: 4 h estimadas, 4 h reais</title><circle class="g-alvo" cx="208.8" cy="218.8" r="12"/><circle class="g-ponto g-azul" cx="208.8" cy="218.8" r="5"/></g>
<g class="marca"><title>#9 Artigo — Introdução e Referencial teórico: 5 h estimadas, 4 h reais</title><circle class="g-alvo" cx="248.0" cy="218.8" r="12"/><circle class="g-ponto g-azul" cx="248.0" cy="218.8" r="5"/></g>
<g class="marca"><title>#25 Gestão — Métricas PSM/CID com dados reais e alinhadas ao modelo: 5 h estimadas, 5,5 h reais</title><circle class="g-alvo" cx="248.0" cy="168.1" r="12"/><circle class="g-ponto g-azul" cx="248.0" cy="168.1" r="5"/></g>
<g class="marca"><title>#3 Fase 1 — Priorização das características, escopo e ODS: 5 h estimadas, 6 h reais</title><circle class="g-alvo" cx="248.0" cy="151.2" r="12"/><circle class="g-ponto g-azul" cx="248.0" cy="151.2" r="5"/></g>
<g class="marca"><title>#2 Fase 1 — Descrição do SuaGradeUnB e modelo de qualidade: 6 h estimadas, 6 h reais
#10 Artigo — Seções da Fase 1 e Fase 2 e revisão final: 6 h estimadas, 6 h reais</title><circle class="g-alvo" cx="287.2" cy="151.2" r="12"/><circle class="g-ponto g-azul" cx="287.2" cy="151.2" r="5"/><text class="g-valor" x="296.2" y="145.2" text-anchor="start">×2</text></g>
<g class="marca"><title>#26 Gestão — Automatizar a coleta das métricas PSM/CID: 8 h estimadas, 8 h reais</title><circle class="g-alvo" cx="365.6" cy="83.6" r="12"/><circle class="g-ponto g-azul" cx="365.6" cy="83.6" r="5"/></g>
<g class="marca"><title>#24 Artigo — Modelo SBC em coluna única e redução do conteúdo da E1: 10 h estimadas, 6 h reais</title><circle class="g-alvo" cx="444.0" cy="151.2" r="12"/><circle class="g-ponto g-azul" cx="444.0" cy="151.2" r="5"/></g>
<text class="g-titulo-eixo" x="248.0" y="392.0" text-anchor="middle">horas estimadas</text>
<text class="g-titulo-eixo" x="14.0" y="185.0" text-anchor="middle" transform="rotate(-90 14 185.0)">horas reais</text>
</svg></div>
<figcaption>Cada ponto é uma issue concluída com estimativa e horas reais (×n = n issues com os mesmos valores). Na linha tracejada a estimativa foi exata. I8 divide a soma das horas reais pela soma das estimadas, então as issues maiores pesam mais.</figcaption>
</figure>

## Evolução semanal

Valores ao fim de cada domingo (23h59) e na data da última coleta.

<figure class="grafico">
<div class="grafico-grade">
<div class="grafico-painel"><p class="grafico-painel-titulo">I1 — PRs revisados no prazo</p><svg viewBox="0 0 340 156" role="img" aria-label="I1 — PRs revisados no prazo"><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">0</text><line class="g-grade" x1="38.0" y1="103.0" x2="292.0" y2="103.0"/><text class="g-tick" x="33.0" y="107.0" text-anchor="end">25</text><line class="g-grade" x1="38.0" y1="74.0" x2="292.0" y2="74.0"/><text class="g-tick" x="33.0" y="78.0" text-anchor="end">50</text><line class="g-grade" x1="38.0" y1="45.0" x2="292.0" y2="45.0"/><text class="g-tick" x="33.0" y="49.0" text-anchor="end">75</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">100</text><line class="g-ref" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-texto-ref" x="296.0" y="20.0" text-anchor="start">meta</text><polyline class="g-linha" points="44.0,85.6 124.7,108.8 205.3,81.2 286.0,71.0"/><g class="marca"><title>18/10: 40,0%
2 de 5 PRs mergeados aprovados antes do merge e em até 48 h</title><circle class="g-alvo" cx="44.0" cy="85.6" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="85.6" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: 20,0%
2 de 10 PRs mergeados aprovados antes do merge e em até 48 h</title><circle class="g-alvo" cx="124.7" cy="108.8" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="108.8" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: 43,8%
7 de 16 PRs mergeados aprovados antes do merge e em até 48 h</title><circle class="g-alvo" cx="205.3" cy="81.2" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="81.2" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: 52,6%
10 de 19 PRs mergeados aprovados antes do merge e em até 48 h</title><circle class="g-alvo" cx="286.0" cy="71.0" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="71.0" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="63.0" text-anchor="start">52,6%</text></svg></div>
<div class="grafico-painel"><p class="grafico-painel-titulo">I2 — PRs aprovados antes do merge</p><svg viewBox="0 0 340 156" role="img" aria-label="I2 — PRs aprovados antes do merge"><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">0</text><line class="g-grade" x1="38.0" y1="103.0" x2="292.0" y2="103.0"/><text class="g-tick" x="33.0" y="107.0" text-anchor="end">25</text><line class="g-grade" x1="38.0" y1="74.0" x2="292.0" y2="74.0"/><text class="g-tick" x="33.0" y="78.0" text-anchor="end">50</text><line class="g-grade" x1="38.0" y1="45.0" x2="292.0" y2="45.0"/><text class="g-tick" x="33.0" y="49.0" text-anchor="end">75</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">100</text><line class="g-ref" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-texto-ref" x="296.0" y="20.0" text-anchor="start">meta</text><polyline class="g-linha" points="44.0,85.6 124.7,108.8 205.3,74.0 286.0,64.8"/><g class="marca"><title>18/10: 40,0%
2 de 5 PRs mergeados</title><circle class="g-alvo" cx="44.0" cy="85.6" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="85.6" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: 20,0%
2 de 10 PRs mergeados</title><circle class="g-alvo" cx="124.7" cy="108.8" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="108.8" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: 50,0%
8 de 16 PRs mergeados</title><circle class="g-alvo" cx="205.3" cy="74.0" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="74.0" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: 57,9%
11 de 19 PRs mergeados</title><circle class="g-alvo" cx="286.0" cy="64.8" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="64.8" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="56.8" text-anchor="start">57,9%</text></svg></div>
<div class="grafico-painel"><p class="grafico-painel-titulo">I3 — Retrabalho (issues)</p><svg viewBox="0 0 340 156" role="img" aria-label="I3 — Retrabalho (issues)"><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">0</text><line class="g-grade" x1="38.0" y1="103.0" x2="292.0" y2="103.0"/><text class="g-tick" x="33.0" y="107.0" text-anchor="end">25</text><line class="g-grade" x1="38.0" y1="74.0" x2="292.0" y2="74.0"/><text class="g-tick" x="33.0" y="78.0" text-anchor="end">50</text><line class="g-grade" x1="38.0" y1="45.0" x2="292.0" y2="45.0"/><text class="g-tick" x="33.0" y="49.0" text-anchor="end">75</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">100</text><polyline class="g-linha" points="44.0,132.0 124.7,132.0 205.3,106.2 286.0,104.4"/><g class="marca"><title>18/10: 0,0%
0 de 9 issues concluídas com a label correcao ou reabertas</title><circle class="g-alvo" cx="44.0" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="132.0" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: 0,0%
0 de 13 issues concluídas com a label correcao ou reabertas</title><circle class="g-alvo" cx="124.7" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="132.0" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: 22,2%
4 de 18 issues concluídas com a label correcao ou reabertas</title><circle class="g-alvo" cx="205.3" cy="106.2" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="106.2" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: 23,8%
5 de 21 issues concluídas com a label correcao ou reabertas</title><circle class="g-alvo" cx="286.0" cy="104.4" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="104.4" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="96.4" text-anchor="start">23,8%</text></svg></div>
<div class="grafico-painel"><p class="grafico-painel-titulo">I4 — Retrabalho (horas)</p><svg viewBox="0 0 340 156" role="img" aria-label="I4 — Retrabalho (horas)"><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">0</text><line class="g-grade" x1="38.0" y1="103.0" x2="292.0" y2="103.0"/><text class="g-tick" x="33.0" y="107.0" text-anchor="end">25</text><line class="g-grade" x1="38.0" y1="74.0" x2="292.0" y2="74.0"/><text class="g-tick" x="33.0" y="78.0" text-anchor="end">50</text><line class="g-grade" x1="38.0" y1="45.0" x2="292.0" y2="45.0"/><text class="g-tick" x="33.0" y="49.0" text-anchor="end">75</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">100</text><polyline class="g-linha" points="44.0,132.0 124.7,132.0 205.3,99.2 286.0,98.0"/><g class="marca"><title>18/10: 0,0%
0 h de 35 h reais registradas em issues concluídas</title><circle class="g-alvo" cx="44.0" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="132.0" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: 0,0%
0 h de 50.5 h reais registradas em issues concluídas</title><circle class="g-alvo" cx="124.7" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="132.0" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: 28,3%
20.5 h de 72.5 h reais registradas em issues concluídas</title><circle class="g-alvo" cx="205.3" cy="99.2" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="99.2" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: 29,3%
22 h de 75 h reais registradas em issues concluídas</title><circle class="g-alvo" cx="286.0" cy="98.0" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="98.0" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="90.0" text-anchor="start">29,3%</text></svg></div>
<div class="grafico-painel"><p class="grafico-painel-titulo">I6 — Desvio de prazo médio (dias)</p><svg viewBox="0 0 340 156" role="img" aria-label="I6 — Desvio de prazo médio (dias)"><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">−10</text><line class="g-grade" x1="38.0" y1="108.8" x2="292.0" y2="108.8"/><text class="g-tick" x="33.0" y="112.8" text-anchor="end">−7,5</text><line class="g-grade" x1="38.0" y1="85.6" x2="292.0" y2="85.6"/><text class="g-tick" x="33.0" y="89.6" text-anchor="end">−5</text><line class="g-grade" x1="38.0" y1="62.4" x2="292.0" y2="62.4"/><text class="g-tick" x="33.0" y="66.4" text-anchor="end">−2,5</text><line class="g-grade" x1="38.0" y1="39.2" x2="292.0" y2="39.2"/><text class="g-tick" x="33.0" y="43.2" text-anchor="end">0</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">2,5</text><line class="g-ref" x1="38.0" y1="39.2" x2="292.0" y2="39.2"/><text class="g-texto-ref" x="296.0" y="43.2" text-anchor="start">prazo</text><polyline class="g-linha" points="44.0,115.3 124.7,102.3 205.3,84.7 286.0,86.5"/><g class="marca"><title>18/10: -8,2 dias
0 de 9 issues concluídas depois do prazo do milestone (negativo = adiantado)</title><circle class="g-alvo" cx="44.0" cy="115.3" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="115.3" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: -6,8 dias
0 de 13 issues concluídas depois do prazo do milestone (negativo = adiantado)</title><circle class="g-alvo" cx="124.7" cy="102.3" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="102.3" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: -4,9 dias
0 de 18 issues concluídas depois do prazo do milestone (negativo = adiantado)</title><circle class="g-alvo" cx="205.3" cy="84.7" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="84.7" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: -5,1 dias
1 de 21 issues concluídas depois do prazo do milestone (negativo = adiantado)</title><circle class="g-alvo" cx="286.0" cy="86.5" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="86.5" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="78.5" text-anchor="start">−5,1</text></svg></div>
<div class="grafico-painel"><p class="grafico-painel-titulo">I8 — Esforço real / estimado</p><svg viewBox="0 0 340 156" role="img" aria-label="I8 — Esforço real / estimado"><rect class="g-faixa" x="38" y="45.0" width="254" height="58.0"/><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">0,8</text><line class="g-grade" x1="38.0" y1="103.0" x2="292.0" y2="103.0"/><text class="g-tick" x="33.0" y="107.0" text-anchor="end">0,9</text><line class="g-grade" x1="38.0" y1="74.0" x2="292.0" y2="74.0"/><text class="g-tick" x="33.0" y="78.0" text-anchor="end">1</text><line class="g-grade" x1="38.0" y1="45.0" x2="292.0" y2="45.0"/><text class="g-tick" x="33.0" y="49.0" text-anchor="end">1,1</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">1,2</text><text class="g-texto-ref" x="296.0" y="49.0" text-anchor="start">0,9 a 1,1</text><polyline class="g-linha" points="44.0,65.3 124.7,88.5 205.3,97.2 286.0,97.2"/><g class="marca"><title>18/10: 1,03
35 h reais / 34 h estimadas em 9 issues com os dois registros</title><circle class="g-alvo" cx="44.0" cy="65.3" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="65.3" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: 0,95
50.5 h reais / 53 h estimadas em 13 issues com os dois registros</title><circle class="g-alvo" cx="124.7" cy="88.5" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="88.5" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: 0,92
72.5 h reais / 78.5 h estimadas em 18 issues com os dois registros</title><circle class="g-alvo" cx="205.3" cy="97.2" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="97.2" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: 0,92
75 h reais / 81.5 h estimadas em 20 issues com os dois registros</title><circle class="g-alvo" cx="286.0" cy="97.2" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="97.2" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="89.2" text-anchor="start">0,92</text></svg></div>
<div class="grafico-painel"><p class="grafico-painel-titulo">I9 — Issues concluídas sem horas reais</p><svg viewBox="0 0 340 156" role="img" aria-label="I9 — Issues concluídas sem horas reais"><line class="g-base" x1="38.0" y1="132.0" x2="292.0" y2="132.0"/><text class="g-tick" x="33.0" y="136.0" text-anchor="end">0</text><line class="g-grade" x1="38.0" y1="16.0" x2="292.0" y2="16.0"/><text class="g-tick" x="33.0" y="20.0" text-anchor="end">1</text><polyline class="g-linha" points="44.0,132.0 124.7,132.0 205.3,132.0 286.0,16.0"/><g class="marca"><title>18/10: 0 issues
de 9 issues concluídas</title><circle class="g-alvo" cx="44.0" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="44.0" cy="132.0" r="4"/></g><text class="g-tick" x="44.0" y="148.0" text-anchor="middle">18/10</text><g class="marca"><title>25/10: 0 issues
de 13 issues concluídas</title><circle class="g-alvo" cx="124.7" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="124.7" cy="132.0" r="4"/></g><text class="g-tick" x="124.7" y="148.0" text-anchor="middle">25/10</text><g class="marca"><title>01/11: 0 issues
de 18 issues concluídas</title><circle class="g-alvo" cx="205.3" cy="132.0" r="12"/><circle class="g-ponto g-azul" cx="205.3" cy="132.0" r="4"/></g><text class="g-tick" x="205.3" y="148.0" text-anchor="middle">01/11</text><g class="marca"><title>05/11: 1 issues
de 21 issues concluídas</title><circle class="g-alvo" cx="286.0" cy="16.0" r="12"/><circle class="g-ponto g-azul" cx="286.0" cy="16.0" r="4"/></g><text class="g-tick" x="286.0" y="148.0" text-anchor="middle">05/11</text><text class="g-valor" x="294.0" y="32.0" text-anchor="start">1</text></svg></div>
</div>
<figcaption>Valor de cada indicador ao fim de cada domingo e na data da última coleta. A linha tracejada marca a meta adotada (I1 e I2) ou o prazo (I6), e a faixa em I8 é o intervalo de 0,90 a 1,10 do critério de decisão. I9 tem meta 0. I3, I4 e I6 ainda não têm limiar definido pela equipe.</figcaption>
</figure>

| Data | PRs revisados no prazo | PRs aprovados antes do merge | Retrabalho (issues) | Retrabalho (horas) | Desvio de prazo médio | Esforço real / estimado | Issues concluídas sem horas reais |
|---|---|---|---|---|---|---|---|
| 18/10 | 40,0% | 40,0% | 0,0% | 0,0% | -8,2 dias | 1,03 | 0 issues |
| 25/10 | 20,0% | 20,0% | 0,0% | 0,0% | -6,8 dias | 0,95 | 0 issues |
| 01/11 | 43,8% | 50,0% | 22,2% | 28,3% | -4,9 dias | 0,92 | 0 issues |
| 05/11 | 52,6% | 57,9% | 23,8% | 29,3% | -5,1 dias | 0,92 | 1 issues |

## Dados brutos

- [issues.csv](evidencias/issues.csv): estimativa, horas reais e desvio de prazo por issue
- [horas.csv](evidencias/horas.csv): registros de horas reais por pessoa
- [prs.csv](evidencias/prs.csv): revisão de cada pull request
- [indicadores.csv](evidencias/indicadores.csv): indicadores em cada data de referência
