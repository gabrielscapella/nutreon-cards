# Gera o Menu Semanal na identidade visual Nutreon (HTML -> PDF A4 via Playwright).
# Uso: python3 gerar.py  -> menu-semanal-gabriel-pereira.html / .pdf
import html, pathlib, subprocess

CLIENTE = "Gabriel Pereira"
DIAS = [
 ("Segunda-feira", [
  ("Café da manhã", ["Ovos mexidos cremosos com queijo minas.", "Pão francês levemente tostado.", "Banana grelhada com canela.", "Café."]),
  ("Lanche da manhã", ["Bolinho de frango com gergelim."]),
  ("Almoço", ["Medalhão de filé-mignon ao molho de mostarda Dijon e ervas frescas.", "Arroz aromático com alho dourado e salsinha.", "Feijão carioca.", "Suflê de abobrinha com toque de limão.", "Salada de folhas com tomate."]),
  ("Sobremesa", ["Mousse aerada de maracujá com claras pasteurizadas e adoçante."]),
  ("Lanche da tarde", ["Milkshake de whey protein com banana, leite desnatado e pasta de amendoim."]),
  ("Jantar", ["Salmão grelhado com crosta de ervas e limão-siciliano.", "Batatas douradas ao alecrim.", "Brócolis salteados no alho."]),
  ("Ceia", ["Panqueca de banana com ovos e canela e calda zero de chocolate."]),
 ]),
 ("Terça-feira", [
  ("Café da manhã", ["Panquecas de banana e ovos.", "Queijo minas.", "Café."]),
  ("Lanche da manhã", ["Iogurte natural com granola e geleia de morango zero."]),
  ("Almoço", ["Fraldinha assada com molho de ervas e mostarda.", "Arroz com cenoura e alho-poró.", "Feijão-preto.", "Vinagrete de maçã verde.", "Batata-doce rústica com páprica.", "Salada de folhas frescas."]),
  ("Sobremesa", ["Gelatina zero açúcar com creme leve de iogurte natural desnatado."]),
  ("Lanche da tarde", ["Sanduíche de frango desfiado com queijo minas e maionese de ovos."]),
  ("Jantar", ["Peito de frango em crosta de castanha e especiarias.", "Purê rústico de batata-doce.", "Legumes salteados."]),
  ("Ceia", ["Shake de whey com leite desnatado e banana, acompanhado de pipoca."]),
 ]),
 ("Quarta-feira", [
  ("Café da manhã", ["Omelete de ovos com queijo minas.", "Bruschetta de pão francês, tomate e ricota.", "Café."]),
  ("Lanche da manhã", ["Muffin proteico de baunilha."]),
  ("Almoço", ["Filé-mignon grelhado com molho cremoso de iogurte natural e mostarda.", "Arroz carreteiro fit.", "Feijão vermelho.", "Cenouras salteadas.", "Salada de folhas com molho de hortelã."]),
  ("Sobremesa", ["Merengue de claras pasteurizadas com morangos frescos e adoçante."]),
  ("Lanche da tarde", ["Crepioca recheada com frango desfiado e requeijão zero."]),
  ("Jantar", ["Penne integral ao molho rústico de tomate e ervas.", "Patinho moído refogado com alho e especiarias.", "Legumes salteados."]),
  ("Ceia", ["Pizza marguerita com massa de frango."]),
 ]),
 ("Quinta-feira", [
  ("Café da manhã", ["Bauruzinho de ovos com pão caseiro.", "Salada de frutas.", "Café."]),
  ("Lanche da manhã", ["Shake proteico de doce de leite caseiro zero."]),
  ("Almoço", ["Strogonoff fit.", "Arroz com cenoura e salsinha.", "Batata-doce em purê.", "Brócolis no vapor finalizados com azeite.", "Salada de folhas frescas."]),
  ("Sobremesa", ["Sorbet artesanal de uva preparado com fruta e adoçante."]),
  ("Lanche da tarde", ["Torta de atum com legumes."]),
  ("Jantar", ["Frango em tiras ao molho oriental leve de gengibre, alho e shoyu.", "Arroz aromatizado com laranja.", "Mix de legumes salteados."]),
  ("Ceia", ["Patê de frango cremoso."]),
 ]),
 ("Sexta-feira", [
  ("Café da manhã", ["Panquecas de chocolate.", "Queijo minas gratinado.", "Café."]),
  ("Lanche da manhã", ["Iogurte natural com granola e frutas."]),
  ("Almoço", ["Contrafilé grelhado com manteiga de ervas em quantidade controlada.", "Arroz com alho tostado e salsinha.", "Farofa de aveia.", "Feijão carioca.", "Batatas rústicas assadas com páprica.", "Salada de folhas com molho leve de mostarda e limão."]),
  ("Sobremesa", ["Creme de mamão com iogurte natural desnatado e canela."]),
  ("Lanche da tarde", ["Sanduíche de frango desfiado com queijo minas e ervas."]),
  ("Jantar", ["Filé de salmão grelhado com molho cítrico.", "Arroz.", "Aspargos grelhados.", "Abobrinha e brócolis salteados."]),
  ("Ceia", ["Sorvete zero de banana."]),
 ]),
]
OBS = ("As porções e a composição nutricional das preparações serão ajustadas conforme a prescrição "
       "individual do nutricionista. As sobremesas são opções leves, sem açúcar adicionado; o valor "
       "calórico varia conforme os ingredientes e as porções.")

e = html.escape
TOTAL = len(DIAS) + 2
LOGO = ('<svg class="mark" viewBox="0 0 40 30" aria-hidden="true">'
        '<polygon points="0,0 9,0 19,15 9,30 0,30 10,15" fill="#12B693"/>'
        '<polygon points="13,0 24,0 34,15 24,30 13,30 23,15" fill="#0C0E0D"/></svg>')

def topo(n):
    return (f'<header class="top"><div class="brand">{LOGO}<span class="name">NUTREON</span>'
            f'<span class="sep"></span><span class="sub">NUTRIÇÃO</span></div>'
            f'<div class="count">{n:02d}/{TOTAL:02d}</div></header>')

def rodape():
    return ('<footer class="foot"><span>GASTRONOMIA PERSONALIZADA · ' + e(CLIENTE.upper()) +
            '</span><span class="links"><b>nutreon.com.br</b><b>@nutreonbr</b></span></footer>')

paginas = []
# Capa
sumario = "".join(f'<li><span class="idx">{i+1:02d}</span><span>{e(d)}</span>'
                  f'<span class="dots"></span><span class="pg">{i+2:02d}</span></li>' for i, (d, _) in enumerate(DIAS))
paginas.append(f'''<section class="page cover">{topo(1)}
<div class="pill">GASTRONOMIA PERSONALIZADA</div>
<div class="cover-body">
  <div class="kicker">PLANO ALIMENTAR · 5 DIAS · 7 REFEIÇÕES/DIA</div>
  <h1>MENU<br><mark>SEMANAL</mark></h1>
  <p class="lead">Cardápio personalizado preparado para <strong>{e(CLIENTE)}</strong>.</p>
  <ol class="toc">{sumario}</ol>
</div>
<div class="glow"></div>{rodape()}</section>''')

for i, (dia, refeicoes) in enumerate(DIAS):
    linhas = ""
    for j, (ref, itens) in enumerate(refeicoes):
        lis = "".join(f"<li>{e(it.rstrip('.'))}</li>" for it in itens)
        linhas += (f'<div class="meal{" main" if ref in ("Almoço","Jantar") else ""}">'
                   f'<div class="label"><span class="n">{j+1:02d}</span>{e(ref.upper())}</div>'
                   f'<ul>{lis}</ul></div>')
    nome, _, sufixo = dia.partition("-")
    paginas.append(f'''<section class="page day">{topo(i+2)}
<div class="day-head"><div class="kicker">DIA {i+1:02d} DE {len(DIAS):02d}</div>
<h2><mark>{e(nome.upper())}</mark>{"-" + e(sufixo.upper()) if sufixo else ""}</h2></div>
<div class="meals">{linhas}</div>
<div class="glow"></div>{rodape()}</section>''')

paginas.append(f'''<section class="page closing">{topo(TOTAL)}
<div class="closing-body">
  <div class="pill">OBSERVAÇÃO</div>
  <h2>CADA PORÇÃO É <mark>AJUSTADA</mark> PARA VOCÊ</h2>
  <p class="lead">{e(OBS)}</p>
  <div class="tags"><span class="tag solid">Sem açúcar adicionado</span><span class="tag">Prescrição individual</span></div>
</div>
<div class="glow"></div>{rodape()}</section>''')

CSS = pathlib.Path(__file__).with_name("estilo.css").read_text()
doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Menu Semanal · {e(CLIENTE)} · Nutreon</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{"".join(paginas)}</body></html>'''

base = pathlib.Path(__file__).parent / "menu-semanal-gabriel-pereira"
base.with_suffix(".html").write_text(doc, encoding="utf-8")
subprocess.run(["node", "-e", f'''
const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{base.with_suffix(".html")}',{{waitUntil:'networkidle'}});await p.evaluate(()=>document.fonts.ready);
await p.pdf({{path:'{base.with_suffix(".pdf")}',format:'A4',printBackground:true,preferCSSPageSize:true}});await b.close();}})();'''], check=True)
print("ok", base.with_suffix(".pdf"))
