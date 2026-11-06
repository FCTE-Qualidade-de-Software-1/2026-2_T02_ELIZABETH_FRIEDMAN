"""Gráficos em SVG da página de indicadores PSM/CID.

O SVG vai direto no Markdown gerado por coletar_metricas_psm.py, sem bibliotecas externas.
Cores e texto usam as classes de docs/stylesheets/graficos.css, que acompanham o tema claro e o escuro.
Cada marca tem um <title> com os dados do item, mostrado ao passar o mouse.
"""
import math
from collections import defaultdict
from html import escape

LARGURA = 720


def num(valor, casas=1):
    valor = round(valor, casas)
    texto = f"{0 if valor == 0 else valor:.{casas}f}"
    if casas:
        texto = texto.rstrip("0").rstrip(".")
    return texto.replace(".", ",").replace("-", "−")


def marcas_eixo(minimo, maximo, quantidade=5, inteiro=False):
    if maximo <= minimo:
        maximo = minimo + 1
    bruto = (maximo - minimo) / quantidade
    potencia = 10 ** math.floor(math.log10(bruto))
    passo = next(m * potencia for m in (1, 2, 2.5, 5, 10) if m * potencia >= bruto)
    if inteiro:
        passo = max(1, round(passo))
    inicio = math.floor(minimo / passo + 1e-9) * passo
    fim = math.ceil(maximo / passo - 1e-9) * passo
    return [round(inicio + i * passo, 6) for i in range(round((fim - inicio) / passo) + 1)]


def escala(d0, d1, r0, r1):
    return lambda v: r0 + (v - d0) * (r1 - r0) / ((d1 - d0) or 1)


def texto(x, y, conteudo, classe="", ancora="start", extra=""):
    c = f' class="{classe}"' if classe else ""
    return f'<text{c} x="{x:.1f}" y="{y:.1f}" text-anchor="{ancora}"{extra}>{escape(conteudo)}</text>'


def linha(x1, y1, x2, y2, classe):
    return f'<line class="{classe}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'


def marca(dica, *elementos):
    return f'<g class="marca"><title>{escape(dica)}</title>{"".join(elementos)}</g>'


def coluna(x, w, y_base, y_topo):
    """Coluna com a ponta arredondada e a base reta."""
    r = min(4, w / 2, y_base - y_topo)
    return (f"M{x:.1f},{y_base:.1f}V{y_topo + r:.1f}Q{x:.1f},{y_topo:.1f} {x + r:.1f},{y_topo:.1f}"
            f"H{x + w - r:.1f}Q{x + w:.1f},{y_topo:.1f} {x + w:.1f},{y_topo + r:.1f}V{y_base:.1f}Z")


def barra(x0, x1, y, h):
    """Barra horizontal com a ponta arredondada e a base reta."""
    r = min(4, h / 2, x1 - x0)
    return (f"M{x0:.1f},{y:.1f}H{x1 - r:.1f}Q{x1:.1f},{y:.1f} {x1:.1f},{y + r:.1f}V{y + h - r:.1f}"
            f"Q{x1:.1f},{y + h:.1f} {x1 - r:.1f},{y + h:.1f}H{x0:.1f}Z")


def figura(elementos, largura, altura, aria, descricao="", legenda=(), largura_max=None):
    """Monta o bloco HTML. Não pode ter linha em branco, senão o Markdown quebra o bloco."""
    partes = ['<figure class="grafico">']
    if legenda:
        itens = "".join(f'<span><i class="{classe}"></i>{escape(nome)}</span>' for classe, nome in legenda)
        partes.append(f'<div class="grafico-legenda">{itens}</div>')
    estilo = f' style="max-width:{largura_max}px"' if largura_max else ""
    partes.append(f'<div class="grafico-rolagem"><svg viewBox="0 0 {largura} {altura:.0f}" role="img" '
                  f'aria-label="{escape(aria)}"{estilo}>')
    partes += elementos
    partes.append("</svg></div>")
    if descricao:
        partes.append(f"<figcaption>{escape(descricao)}</figcaption>")
    partes.append("</figure>")
    return "\n".join(partes)


def colunas(itens, titulo_eixo, aria, descricao, legenda, referencia=None):
    """Uma coluna por item. itens: dicts com rotulo, valor (None = sem valor), classe e dica.
    referencia: (valor, texto) de uma linha de limite."""
    esq, dir_, topo, base, altura = 44, 12, 30, 28, 270
    y_base = altura - base
    valores = [i["valor"] for i in itens if i["valor"] is not None]
    marcas = marcas_eixo(0, max(valores + [referencia[0] if referencia else 0, 1]))
    y = escala(0, marcas[-1], y_base, topo)
    banda = (LARGURA - esq - dir_) / max(len(itens), 1)
    w = min(24, banda * 0.72)
    el = [texto(esq, 12, titulo_eixo, "g-titulo-eixo")]
    for m in marcas:
        el.append(linha(esq, y(m), LARGURA - dir_, y(m), "g-grade" if m else "g-base"))
        el.append(texto(esq - 6, y(m) + 4, num(m), "g-tick", "end"))
    passo_rotulo = max(1, math.ceil(len(itens) / ((LARGURA - esq - dir_) // 32)))
    for k, item in enumerate(itens):
        x0 = esq + k * banda
        cx = x0 + banda / 2
        alvo = f'<rect class="g-alvo" x="{x0:.1f}" y="{topo}" width="{banda:.1f}" height="{y_base - topo}"/>'
        if item["valor"] is None:
            desenho = f'<path class="g-x {item["classe"]}" d="M{cx - 4:.1f},{y_base - 12:.1f}l8,8m0,-8l-8,8"/>'
        else:
            topo_coluna = min(y(item["valor"]), y_base - 2)
            desenho = f'<path class="{item["classe"]}" d="{coluna(cx - w / 2, w, y_base, topo_coluna)}"/>'
        el.append(marca(item["dica"], alvo, desenho))
        if k % passo_rotulo == 0:
            el.append(texto(cx, y_base + 16, item["rotulo"], "g-tick", "middle"))
    if referencia:
        yr = y(referencia[0])
        el.append(linha(esq, yr, LARGURA - dir_, yr, "g-ref"))
        el.append(texto(LARGURA - dir_, yr - 5, referencia[1], "g-texto-ref", "end"))
    return figura(el, LARGURA, altura, aria, descricao, legenda)


def grade_issues(grupos, aria, descricao, legenda):
    """Um quadrado por issue, uma linha por milestone.
    grupos: dicts com titulo, subtitulo, resumo e issues = [(numero, concluida, dica)]."""
    esq, dir_, lado, gap = 176, 110, 26, 4
    por_linha = max(1, (LARGURA - esq - dir_) // (lado + gap))
    el, y = [], 4
    for g in grupos:
        el.append(texto(0, y + 12, g["titulo"][:26], "g-rotulo"))
        el.append(texto(0, y + 27, g["subtitulo"], "g-tick"))
        el.append(texto(LARGURA, y + 17, g["resumo"], "g-valor", "end"))
        for k, (numero, concluida, dica) in enumerate(g["issues"]):
            cx = esq + (k % por_linha) * (lado + gap)
            cy = y + (k // por_linha) * (lado + gap)
            classe = "g-chip-feita" if concluida else "g-chip-aberta"
            el.append(marca(dica,
                            f'<rect class="{classe}" x="{cx}" y="{cy}" width="{lado}" height="{lado}" rx="4"/>',
                            texto(cx + lado / 2, cy + 17, str(numero), f"{classe}-texto", "middle")))
        linhas_chips = max(1, math.ceil(len(g["issues"]) / por_linha))
        y += max(linhas_chips * (lado + gap), 34) + 12
    return figura(el, LARGURA, y, aria, descricao, legenda)


def pontos_empilhados(pontos, titulo_eixo, aria, descricao, legenda):
    """Um ponto por item, empilhados quando o valor (inteiro) se repete.
    pontos: dicts com valor, classe e dica, já na ordem de empilhamento."""
    esq, dir_, topo, base, passo, r = 16, 16, 30, 46, 15, 6
    minimo = min([p["valor"] for p in pontos] + [-1])
    maximo = max([p["valor"] for p in pontos] + [1])
    banda = (LARGURA - esq - dir_) / (maximo - minimo + 1)
    pilhas = defaultdict(list)
    for p in pontos:
        pilhas[p["valor"]].append(p)
    y_base = topo + max(max(len(v) for v in pilhas.values()) * passo + 6, 60)
    altura = y_base + base
    x = escala(minimo - 0.5, maximo + 0.5, esq, LARGURA - dir_)
    el = [linha(x(0), topo - 8, x(0), y_base, "g-ref"),
          texto(x(0), topo - 14, "prazo do milestone", "g-texto-ref", "middle")]
    for valor, pilha in pilhas.items():
        for k, p in enumerate(pilha):
            cy = y_base - r - 4 - k * passo
            el.append(marca(p["dica"],
                            f'<circle class="g-alvo" cx="{x(valor):.1f}" cy="{cy:.1f}" r="{max(r + 2, banda / 2):.1f}"/>',
                            f'<circle class="g-ponto {p["classe"]}" cx="{x(valor):.1f}" cy="{cy:.1f}" r="{r}"/>'))
    el.append(linha(esq, y_base, LARGURA - dir_, y_base, "g-base"))
    a_cada = 1 if banda >= 24 else 2 if banda >= 12 else 5
    for v in range(minimo, maximo + 1):
        if v % a_cada == 0:
            el.append(texto(x(v), y_base + 16, (num(v, 0) if v <= 0 else f"+{v}"), "g-tick", "middle"))
    el.append(texto(LARGURA / 2, y_base + 36, titulo_eixo, "g-titulo-eixo", "middle"))
    return figura(el, LARGURA, altura, aria, descricao, legenda)


def barras_horizontais(itens, aria, descricao, referencia=None):
    """Uma barra por item. itens: dicts com rotulo, valor, texto_valor e dica.
    referencia: (valor, texto) de uma linha vertical."""
    esq, dir_, topo, altura_linha, h = 168, 112, 28, 30, 16
    marcas = marcas_eixo(0, max([i["valor"] for i in itens] + [referencia[0] if referencia else 0, 1]))
    x = escala(0, marcas[-1], esq, LARGURA - dir_)
    y_fim = topo + altura_linha * len(itens)
    el = []
    for m in marcas:
        el.append(linha(x(m), topo - 4, x(m), y_fim, "g-grade" if m else "g-base"))
        el.append(texto(x(m), y_fim + 16, num(m), "g-tick", "middle"))
    if referencia:
        xr = x(referencia[0])
        el.append(linha(xr, topo - 8, xr, y_fim, "g-ref"))
        el.append(texto(xr, topo - 13, referencia[1], "g-texto-ref", "middle"))
    for k, item in enumerate(itens):
        y = topo + k * altura_linha + (altura_linha - h) / 2
        alvo = f'<rect class="g-alvo" x="0" y="{y - 6:.1f}" width="{LARGURA}" height="{h + 12}"/>'
        el.append(marca(item["dica"], alvo,
                        texto(esq - 10, y + 12, item["rotulo"][:24], "g-rotulo", "end"),
                        f'<path class="g-azul" d="{barra(esq, max(x(item["valor"]), esq + 2), y, h)}"/>',
                        texto(x(item["valor"]) + 8, y + 12, item["texto_valor"], "g-valor")))
    return figura(el, LARGURA, y_fim + 26, aria, descricao)


def dispersao(pontos, titulo_x, titulo_y, aria, descricao):
    """Um ponto por item; itens com o mesmo par de valores viram um ponto só, com a contagem ao lado.
    pontos: dicts com x, y e dica."""
    largura, altura = 460, 400
    esq, dir_, topo, base = 52, 16, 16, 46
    maximo = max([p["x"] for p in pontos] + [p["y"] for p in pontos] + [1])
    marcas = marcas_eixo(0, maximo)
    sx = escala(0, marcas[-1], esq, largura - dir_)
    sy = escala(0, marcas[-1], altura - base, topo)
    el = []
    for m in marcas:
        el.append(linha(sx(m), topo, sx(m), altura - base, "g-grade" if m else "g-base"))
        el.append(linha(esq, sy(m), largura - dir_, sy(m), "g-grade" if m else "g-base"))
        el.append(texto(sx(m), altura - base + 16, num(m), "g-tick", "middle"))
        el.append(texto(esq - 6, sy(m) + 4, num(m), "g-tick", "end"))
    fim = marcas[-1]
    el.append(linha(sx(0), sy(0), sx(fim), sy(fim), "g-ref"))
    el.append(texto(sx(fim * 0.8) + 8, sy(fim * 0.8) + 14, "real = estimado", "g-texto-ref"))
    el.append(texto(esq + 8, topo + 14, "acima da linha: levou mais que o estimado", "g-dica-canto"))
    el.append(texto(largura - dir_ - 8, altura - base - 8, "abaixo: levou menos", "g-dica-canto", "end"))
    grupos = defaultdict(list)
    for p in pontos:
        grupos[(p["x"], p["y"])].append(p["dica"])
    for (vx, vy), dicas in sorted(grupos.items()):
        cx, cy = sx(vx), sy(vy)
        elementos = [f'<circle class="g-alvo" cx="{cx:.1f}" cy="{cy:.1f}" r="12"/>',
                     f'<circle class="g-ponto g-azul" cx="{cx:.1f}" cy="{cy:.1f}" r="5"/>']
        if len(dicas) > 1:
            elementos.append(texto(cx + 9, cy - 6, f"×{len(dicas)}", "g-valor"))
        el.append(marca("\n".join(dicas), *elementos))
    el.append(texto((esq + largura - dir_) / 2, altura - 8, titulo_x, "g-titulo-eixo", "middle"))
    y_meio = (topo + altura - base) / 2
    el.append(texto(14, y_meio, titulo_y, "g-titulo-eixo", "middle", f' transform="rotate(-90 14 {y_meio:.1f})"'))
    return figura(el, largura, altura, aria, descricao, largura_max=largura)


def painel_linha(titulo, pontos, formato, dominio, referencia=None, faixa=None, inteiro=False):
    """Pequeno gráfico de linha da evolução de um indicador.
    pontos: [(rotulo_data, valor ou None, dica)]. referencia: (valor, texto). faixa: (de, até, texto)."""
    largura, altura = 340, 156
    esq, dir_, topo, base = 38, 54, 16, 24
    marcas = marcas_eixo(*dominio, quantidade=4, inteiro=inteiro)
    sy = escala(marcas[0], marcas[-1], altura - base, topo)
    sx = escala(0, max(len(pontos) - 1, 1), esq + 6, largura - dir_)
    el = []
    if faixa:
        el.append(f'<rect class="g-faixa" x="{esq}" y="{sy(faixa[1]):.1f}" width="{largura - dir_ + 6 - esq}" '
                  f'height="{sy(faixa[0]) - sy(faixa[1]):.1f}"/>')
    for m in marcas:
        el.append(linha(esq, sy(m), largura - dir_ + 6, sy(m), "g-grade" if m != marcas[0] else "g-base"))
        el.append(texto(esq - 5, sy(m) + 4, num(m, 2), "g-tick", "end"))
    if faixa:
        el.append(texto(largura - dir_ + 10, sy(faixa[1]) + 4, faixa[2], "g-texto-ref"))
    if referencia:
        el.append(linha(esq, sy(referencia[0]), largura - dir_ + 6, sy(referencia[0]), "g-ref"))
        el.append(texto(largura - dir_ + 10, sy(referencia[0]) + 4, referencia[1], "g-texto-ref"))
    trechos, atual = [], []
    for k, (_, valor, _) in enumerate(pontos):
        if valor is None:
            if atual:
                trechos.append(atual)
            atual = []
        else:
            atual.append(f"{sx(k):.1f},{sy(valor):.1f}")
    if atual:
        trechos.append(atual)
    for t in trechos:
        el.append(f'<polyline class="g-linha" points="{" ".join(t)}"/>')
    a_cada = max(1, math.ceil(len(pontos) / 6))
    for k, (rotulo, valor, dica) in enumerate(pontos):
        if valor is not None:
            el.append(marca(dica, f'<circle class="g-alvo" cx="{sx(k):.1f}" cy="{sy(valor):.1f}" r="12"/>',
                            f'<circle class="g-ponto g-azul" cx="{sx(k):.1f}" cy="{sy(valor):.1f}" r="4"/>'))
        if k % a_cada == 0 or k == len(pontos) - 1:
            el.append(texto(sx(k), altura - base + 16, rotulo, "g-tick", "middle"))
    ultimos = [(k, v) for k, (_, v, _) in enumerate(pontos) if v is not None]
    if ultimos and not (referencia and abs(sy(ultimos[-1][1]) - sy(referencia[0])) < 12):
        k, v = ultimos[-1]
        y_rotulo = sy(v) - 8 if sy(v) - 8 >= 12 else sy(v) + 16
        el.append(texto(sx(k) + 8, y_rotulo, formato(v), "g-valor"))
    return (f'<div class="grafico-painel"><p class="grafico-painel-titulo">{escape(titulo)}</p>'
            f'<svg viewBox="0 0 {largura} {altura}" role="img" aria-label="{escape(titulo)}">'
            + "".join(el) + "</svg></div>")


def paineis(lista, descricao):
    return "\n".join(['<figure class="grafico">', '<div class="grafico-grade">', *lista, "</div>",
                      f"<figcaption>{escape(descricao)}</figcaption>", "</figure>"])
