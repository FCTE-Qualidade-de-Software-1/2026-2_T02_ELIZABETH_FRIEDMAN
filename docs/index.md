# Avaliação de Qualidade de Produto de Software

Este site documenta o projeto final da equipe **Elizabeth Friedman** na disciplina
FGA0315 — Qualidade de Software 1 (UnB/FCTE, 2026/2, Turma T02, Profa. Cristiane Soares Ramos).

O projeto avalia a qualidade do produto **Sua Grade UnB** seguindo o processo de
avaliação da família SQuaRE (ISO/IEC 25040), com o modelo de qualidade da ISO/IEC 25010
e métricas definidas pelo método *Goal–Question–Metric* (GQM).

## Produto avaliado

O [Sua Grade UnB](https://suagradeunb.com.br/) é uma aplicação web que ajuda estudantes da
Universidade de Brasília a montar a grade horária do semestre. O estudante busca disciplinas
por nome ou código, seleciona as que deseja cursar e o sistema gera combinações de turmas sem
conflito de horário, que podem ser salvas na conta do usuário ou no próprio navegador. Os dados de turmas são obtidos por *web scraping* das turmas do SIGAA.

O sistema foi desenvolvido no segundo semestre de 2023 por seis estudantes na disciplina de Métodos de Desenvolvimento de Software (MDS) e é open source.

Repositório disponível em: [unb-mds/2023-2-SuaGradeUnB](https://github.com/unb-mds/2023-2-SuaGradeUnB).


## Percurso por objetivo

Cada página segue um objetivo de medição do começo ao fim: definição, questões e hipóteses, métricas,
método, dados, resultados e julgamento.

| Objetivo | O que se quer saber | Questões e métricas | Estado | Ir direto para |
|----------|---------------------|---------------------|--------|----------------|
| [**G1 — Manutenibilidade**](objetivo-g1.md) | Mantenedores e contribuidores conseguem compreender, modificar e testar o código? | Q1.1 a Q1.4, M1.1 a M1.4 | Inconclusivo: falta medida válida de M1.3 | [Definição](fase-2.md#g1-manutenibilidade) · [Dados](fase-4.md#dados-g1) · [Resultados](fase-4.md#21-g1-manutenibilidade) |
| [**G2 — Eficiência de desempenho**](objetivo-g2.md) | O estudante recebe resposta em tempo aceitável ao buscar, selecionar, gerar e salvar? | Q2 a Q5, M2 a M5 | Atendido nas condições avaliadas | [Definição](fase-2.md#g2-eficiencia-de-desempenho) · [Dados](fase-4.md#dados-g2) · [Resultados](fase-4.md#22-g2-eficiencia-de-desempenho) |
| [**G3 — Capacidade de interação**](objetivo-g3.md) | O estudante aprende o fluxo, controla as escolhas, não perde a grade e entende a interface? | Q6 a Q9, M6 a M9 | Não atendido | [Definição](fase-2.md#g3-capacidade-de-interacao-usabilidade) · [Dados](fase-4.md#dados-g3) · [Resultados](fase-4.md#23-g3-capacidade-de-interacao) |

A visão dos três juntos está no [diagrama GQM](fase-2.md#5-diagrama-gqm) e no
[julgamento por objetivo](fase-4.md#31-estado-de-cada-hipotese-e-de-cada-objetivo).

## Como navegar por fase

| Etapa | Conteúdo | Situação |
|-------|----------|----------|
| [Fase 1 — Requisitos da avaliação](fase-1.md) | Propósito, partes interessadas, modelo de qualidade, características priorizadas e escopo | Concluída |
| [Fase 2 — Especificação](fase-2.md) | Objetivos, questões, hipóteses e métricas (GQM); níveis de pontuação e critérios de julgamento | Concluída |
| [Fase 3 — Projeto da avaliação](fase-3.md) | Método, recursos, ambiente e cronograma | Concluída |
| [Fase 4 — Execução e resultados](fase-4.md) | Medições, análise, julgamento e ação de melhoria | Concluída |
| [Gestão do projeto](gestao/metricas.md) | Métricas PSM/CID e [atas de reunião](gestao/atas.md) | Em constante evolução |

## Links rápidos

- Repositório: <https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN>
- Releases e artigo: [Entregas](entregas.md)
- Equipe e contribuições: [Equipe](equipe.md)
- Declaração de uso de IA: [Uso de IA](uso-de-ia.md)
