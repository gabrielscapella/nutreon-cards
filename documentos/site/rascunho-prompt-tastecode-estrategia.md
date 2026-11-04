> **Rascunho bruto nº 2 de 5 (lente: estratégia de marca e copy).** Versão preliminar entregue a pedido do Gabriel enquanto o painel (júri + síntese + críticos) finaliza o prompt definitivo. Fatos conferidos no site em 04/11/2026.

# Redesenho do site nutreon.com.br — briefing único

Você vai redesenhar o site da Nutreon. Este texto é o único briefing que você recebe; leia inteiro antes de abrir o navegador. Você roda no Mac do Gabriel Scapella (CEO e fundador), com internet: audite o site ao vivo, baixe as fotos reais, confira cada número. Quando faltar informação, pergunte ao Gabriel. Nunca invente.

O padrão é "site de 70 mil dólares, feito pelos melhores do mundo". Isso não se mede em efeito visual; mede-se em precisão. A Nutreon ganha autoridade por precisão, não por grito. Seu trabalho é fazer essa precisão dar tesão.

## 1. Quem é a Nutreon e o que ela tem que ninguém tem

Nutreon® é uma marca brasileira de suplementos (Anápolis-GO, setembro de 2025, 4 pessoas, CNPJ 62.577.922/0001-13). Vende 17 produtos pela Nuvemshop, de whey e creatina a pré-treino, articulações, polivitamínico e kits.

O setor vende promessa. A Nutreon vende **o que dá para verificar**. São cinco provas, e nenhum concorrente tem as cinco juntas. O site existe para torná-las visíveis e navegáveis:

1. **O rótulo inteiro está na página.** Composição por porção com %VD, ingredientes, alérgicos, modo de uso, avisos e a seção "O que não leva". Do jeito que está no pote, antes de você pagar.
2. **A dose do produto aparece lado a lado com a dose dos estudos.** "Por que esta dose" em cada PDP, com fonte (posições da ISSN: Jäger et al. 2017; Kreider et al. 2017; Guest et al. 2021). Estudos usam 3 a 5 g de creatina por dia; uma porção Nutreon entrega 3 g.
3. **Todo lote é testado e tem número impresso no pote.** Frase oficial, repetida sem alterar: "Todos os lotes são testados com rigor de farmacopeia americana e todos os produtos têm rastreabilidade completa."
4. **Nutreon Pro sem comissão e sem meta.** Programa para CRN, CRM e CREF. Quem prescreve não ganha nada com a compra do paciente. Conflito de interesse do fundador declarado na página.
5. **Um blog com a mesma régua para o resultado que ajuda e para o que atrapalha a venda.** O "Nutreon Ciência" publicou que vitamina D não evitou fratura em 25.871 adultos e que o teto de 1,62 g/kg/dia de proteína vem de uma curva sem significância estatística. Referência ABNT, IC 95%, risco de viés, financiamento, selo de evidência, caixa de conflito de interesse. Sem antes e depois, sem depoimento.

**A ideia-mãe para levar ao Taste Skill:** *a página é o rótulo*. Não é uma loja que explica; é um laboratório que vende. Formule sua própria "ideia em uma frase", mas ela precisa caber dentro desta.

## 2. A equipe que você encarna

Orçamento infinito, todos sêniores, os melhores do mundo. Cada um passa por toda decisão e pode reprovar.

- **Diretor(a) de criação**: exige a ideia em uma frase; reprova tela que serviria a outra marca trocando o logo.
- **Estrategista de marca**: cada seção prova uma das cinco provas. Seção que só decora, sai.
- **Diretor(a) de arte editorial** (revista de ciência): números são os heróis; hierarquia tipográfica de verdade.
- **Designer de produto para e-commerce**: home → "Comprar" em até 3 cliques; PDP que vende sem esconder a tabela; mobile primeiro.
- **Copywriter sênior em português do Brasil**: dono da régua da seção 7; veta clichê, exclamação, emoji e adjetivo sem número.
- **Diretor(a) de fotografia**: dono da shot list; proíbe mockup.
- **Engenheiro(a) front-end sênior**: Lighthouse, CLS, `prefers-reduced-motion`, semântica, teclado.
- **Especialista Nuvemshop**: o que o tema permite, o que só o headless resolve, o que quebra no checkout.
- **Consultor(a) regulatório** (ANVISA, CFN/CFM/CONFEF): lê toda frase antes de ir ao ar.
- **Editor(a) científico**: confere forest plot, IC 95%, barra de evidência, referência; não aceita número fora do site ou da fonte.
- **QA de slop**: roda a seção 13 em cada tela, em 3 larguras.

## 3. Processo (nesta ordem)

### 3.1 Auditar o site ao vivo
Navegue todas as páginas do menu e do rodapé, todas as PDPs, as 4 páginas de Ciência, os 3 posts e as 3 páginas do Pro. Registre em `auditoria.md` duas listas:

- **Conteúdo excelente, preservar palavra por palavra**: tabelas, "Por que esta dose", "O que não leva", regras do Pro, "Como trabalhamos" do blog.
- **O que denuncia template barato**: pop-up "Desconto exclusivo!", barra de avisos rolante, badge "Grátis" em todo card, "-0% OFF" sem desconto, lista de 12 parcelas e meios de pagamento pesando a PDP, institucionais sem hierarquia, `/nosso-clean-label/` e `/nutreon-pro-laudo/` duplicando Manifesto e Qualidade, `/lista-vip/` em 404, link do X quebrado, "Nutreon LABS"/"NutreON", Archivo 400/700 sem escala, e o maior problema: **todas as fotos de produto são renders 3D de mockup** em fundo cinza, com reflexo plástico, sombra falsa, um selo "TECNOLOGIA LHA" carimbado por cima e linguagem visual inconsistente entre produtos (whey em pote branco com arte de "splash", Creatina/Iso/Muscle On em pote preto com degradê teal, Complex verde, OnFire rosa ou verde-limão).

Baixe as 3 fotos de cada produto do CDN (`https://acdn-us.mitiendanube.com/stores/006/551/118/products/<slug>-1-...webp`) e avalie fundo, recorte, resolução, luz e o carimbo. Anote quais servem como provisórias e em que tamanho; nenhuma serve como herói.

### 3.2 Perguntas ao Gabriel (antes de desenhar uma linha)
Todas de uma vez, em `perguntas.md`; espere a resposta:

1. Posso publicar laudos por lote (PDF ou consulta por número), ou a frase oficial é o limite hoje?
2. Fabricação própria ou terceirizada? Posso dizer isso no site? (Sem resposta, não afirme nada sobre fábrica.)
3. Existem fotos em alta além das do CDN? Bastidores, laboratório, embalagem, equipe?
4. Confirma "Nutreon" como único nome, eliminando "LABS" e "NutreON" de textos e slugs?
5. Prioridade comercial para a home: Whey, Creatina ou Kit On Essencial?
6. Rota A ou rota B (seção 10)? Quem mantém o site depois? Há prazo?
7. Newsletter: manter? Qual ferramenta? "Radar Nutreon" existe ou é projeto?
8. O cadastro do Pro continua em `prescritor.nutreon.com.br`? Redesenho só a landing e a biblioteca?
9. Comunidade: há histórias autorizadas por escrito? Se não, a página vira uma chamada honesta ou sai do menu?
10. Regras exatas de frete grátis e 5% no Pix para o aviso do topo.
11. Aceita títulos-pergunta na home, no tom dos cards, ou prefere só afirmativo?
12. As fotos atuais são renders 3D com o selo "LHA" carimbado. Existem os arquivos de arte das embalagens ou renders em alta sem o carimbo? Há previsão de ensaio fotográfico real (eu entrego a shot list)? Topa discutir a padronização visual dos rótulos entre os produtos? Sem resposta, trato todas as fotos como provisórias.

### 3.3 Apresentar direções antes de construir
Siga o Taste Skill: liste "o que só a Nutreon tem" (deve bater com as cinco provas), sorteie 3 das 20 direções e apresente as 3 em `direcoes/`, cada uma com ideia em uma frase, paleta derivada com contraste calculado (seção 5), tipo de hero, e uma tela da home e uma da PDP em média fidelidade, em 1440 e 390 px. Recomende uma. No mesmo documento, apresente a decisão de plataforma (seção 10). Espere o Gabriel escolher.

### 3.4 Construir
Protótipo navegável estático de alta fidelidade (HTML/CSS/JS ou Astro), com dados reais do site ao vivo, fotos reais e o copy deck. É ele que valida o design; o porte vem depois.

### 3.5 Auto-revisão
Teste em 390, 820 e 1440 px, com screenshot de cada página. Rode as seções 12 e 13. Corrija e repita até 3 rodadas.

## 4. Identidade: o que preservar e o que evoluir

Olhe os três cards oficiais do blog (a linguagem que o Gabriel aprova). A identidade dos cards é a boa; o tema Toluca a diluiu.

**Preservar sem negociar:**
- Verde Nutreon `#12B693` como única assinatura; preto `#0C0E0D`; base clara com grid fino quase invisível e brilho radial verde-menta no canto inferior direito.
- Logo: dois chevrons duplos (um verde, um preto) + wordmark NUTREON® em grotesca pesada, caixa alta, tracking largo. Variante "NUTREON | CIÊNCIA" no blog.
- Tipografia: títulos em grotesca muito pesada (Archivo Black ou 900), caixa alta, tracking negativo, entrelinha apertada; corpo em grotesca regular; metadados, numeração ("01/06"), eixos e unidades em mono (JetBrains Mono ou IBM Plex Mono) com tracking largo.
- Recursos: **palavra-chave do título em bloco sólido verde** (texto preto por cima); pílula preta com texto verde ("ANÁLISE CRÍTICA"); botão pílula verde sólido e pílula de contorno preto; numeração em círculo verde; forest plot com IC 95%; **barra de evidência em 4 segmentos** (muito baixa / baixa / moderada / alta).
- Tom direto, transparência, disclaimer em toda página.

**Evoluir:**
- De "um verde + preto + branco" para um sistema com profundidade (seção 5) e escala tipográfica editorial: display gigante, números maiores que títulos, mono para dados.
- Fotografia real entra pela primeira vez (seção 6); institucionais ganham a estrutura dos cards: numeração, pílulas, highlights, tabelas.

## 5. Cor e tipo: direção concreta

Proponha 2 ou 3 paletas derivadas, com amostras e contraste WCAG calculado, antes de aplicar. Regras:

- **Verde Nutreon `#12B693`**: bloco de highlight atrás de palavra (texto preto), botão primário (texto preto), traço de gráfico. **Nunca texto pequeno sobre claro**: contraste de cerca de 2,5:1, reprova. Texto verde só sobre escuro.
- **Verde elétrico** (faixa `#2EE6B6`–`#3DF2BE`): só sobre escuro, para highlight, foco de teclado e números-herói; meça ≥ 4,5:1.
- **Verde profundo** (faixa `#0B5E4C`–`#07463A`): ênfase sobre claro (≥ 4,5:1 sobre papel), bordas.
- **Verde-tinta quase preto** (faixa `#061F1A`–`#0A1C18`): fundo das seções escuras "laboratório", no lugar do preto puro, com grid em opacidade baixa e brilho radial elétrico. O site alterna: home e PDP em papel, Qualidade e Ciência em laboratório, blog em papel.
- **Papel**: off-white levemente quente (`#F7F6F1`–`#FAF9F5`) no lugar do branco puro. Grid `#E6E6E6` a 40–60% de opacidade, passo de 48 ou 64 px.
- **Preto `#0C0E0D`** para texto; **cinza `#7D8180`** para metadados (confira ≥ 4,5:1); **`#E6E6E6`** para barras vazias e divisórias.
- **Um único tom de aviso**, âmbar escuro contido, para cafeína e alérgicos. Nenhum outro matiz.

**Tipografia**: duas famílias e uma mono, em tokens. Display com `clamp()` de 56 px (390) a 144 px (1440), peso 900, tracking −0,02 a −0,04 em, entrelinha 0,9–0,95; números-herói maiores que o display da seção; corpo 17–18 px, entrelinha 1,5; mono 12–13 px, tracking +0,08 em, caixa alta. Nada de Inter ou Roboto em display.

## 6. Fotografia e imagem

Proibido: mockup 3D genérico; pote flutuando com brilho ou reflexo falso; respingo, raio, fogo, partícula; banco de imagens de academia (pessoa sorrindo com shake, neon, halteres cromados); antes e depois; ícones de linha em círculos coloridos; ilustração vetorial corporativa.

As fotos da loja hoje são renders de mockup (pergunta 12): são exatamente o que o Gabriel não quer ver. Enquanto não existir fotografia real, use-as como **provisórias e discretas**: recorte o pote, remova o carimbo "LHA", assente sobre papel ou laboratório com **sombra de contato única e uniforme** para todos os produtos, nunca brilho adicionado, e só em tamanho de card ou de galeria de PDP. **Nunca como herói.** O herói da home, de Qualidade e de Ciência vem da shot list abaixo (macro de textura, balança, rótulo com lote) ou é tipográfico, com número gigante. Quando a fotografia real existir, o pote volta grande.

Onde faltar imagem, use coleções abertas (Unsplash, Pexels) com crédito, marcadas `PROVISÓRIA` no `alt` e em `fotografia/provisorias.md`, seguindo esta **shot list**, que também é o briefing do ensaio real:

1. Pote em luz dura lateral, sombra longa, fundo papel; 4:5 e 16:9.
2. Macro de textura do pó (whey chocolate, cristal de creatina, OnFire uva verde) com dosador no quadro.
3. Rótulo em close legível; número de lote em foco.
4. Balança de precisão com 30 g pesados; vidraria limpa; ninguém sorrindo.
5. Mão segurando dosador, pele real.
6. Treino real: barra carregada, suor, luz natural; sem pose, sem olhar para a câmera, sem marca de terceiros.
7. Flat lay dos 3 produtos do Kit On Essencial sobre papel com grid impresso.
8. Bastidores de conferência de lote: só se existir e com autorização por escrito.

Para cada item: proporção, luz, fundo. Retoque mínimo.

## 7. Voz e copy (régua obrigatória)

É aqui que um site de 70 mil dólares se separa de um template. A voz já existe nos cards e no blog: direta, técnica sem jargão vazio, questionadora, com número grande.

### 7.1 Arquitetura de mensagem (três andares)
- **Promessa**, uma frase repetida em todo lugar: "Sem promessa que o rótulo não sustente."
- **Provas**: as cinco da seção 1; cada página principal prova pelo menos uma, com dado real.
- **Produto**: cada produto tem uma linha de 3 a 5 números e zero adjetivos.

### 7.2 Dez regras de voz
1. Número antes do adjetivo. Sem número, quase sempre sem adjetivo: "22 g de proteína em 30 g", nunca "proteína de alta qualidade".
2. Pergunta quando há dúvida real; afirmação quando há dado. Nunca pergunta retórica de venda ("Quer mais resultado?").
3. Frases curtas. Ponto final. Sem exclamação. Sem emoji (os botões com emoji do blog viram texto com ícone de marca).
4. Uma palavra por título recebe o bloco verde: a que carrega o peso ("FRATURA", "pequeno", "CONSULTA").
5. Caixa alta só em display e pílulas.
6. Toda afirmação tem fonte ou está no rótulo. Sem um dos dois, corta.
7. "Você" com quem compra; "profissional" no Pro. Nunca "atleta de elite", "guerreiro", "monstro".
8. Verbos concretos no lugar de marketing: mostramos, testamos, citamos, não prometemos.
9. Tipografia correta: aspas curvas (“ ”), travessão (—), espaço antes de unidade (22 g, 200 mg, R$ 279), vírgula decimal (2,49 kg), ponto de milhar (25.871), "IC 95%".
10. O nome é **Nutreon**. Sempre. "Nutreon Pro", "Nutreon Ciência". Nunca "LABS" nem "NutreON". Rode um grep no final.

### 7.3 Banco de títulos (use, adapte, não baixe a régua)
Hero da home (ofereça os três ao Gabriel):
- **O RÓTULO INTEIRO ESTÁ NA PÁGINA. ANTES DO "COMPRAR".**
- **DOSE CLARA. RÓTULO INTEIRO. LOTE RASTREÁVEL.** (o atual)
- **QUANTO TEM NO POTE? QUANTO OS ESTUDOS USARAM? MOSTRAMOS OS DOIS.**
Sub do hero, manter: "Composição por porção, modo de uso e avisos do rótulo em cada página. Sem promessa que o rótulo não sustente."

As cinco provas na home:
- **O RÓTULO INTEIRO, NA PÁGINA.** Tabela com %VD, ingredientes, alérgicos, avisos. Do jeito que está no pote.
- **A DOSE, LADO A LADO COM A DOS ESTUDOS.** Creatina: estudos, 3 a 5 g por dia. Nutreon: 3 g por porção. Fonte: Kreider et al., 2017.
- **TODO LOTE TESTADO. NÚMERO IMPRESSO NO POTE.** Rigor de farmacopeia americana. Rastreabilidade completa.
- **PRO SEM COMISSÃO. SEM META.** Quem prescreve Nutreon não ganha nada com isso. É regra do programa.
- **A MESMA RÉGUA PARA O QUE AJUDA E PARA O QUE ATRAPALHA A VENDA.** Vitamina D não evitou fratura em 25.871 adultos. Publicamos assim mesmo.

Linhas de produto:
- Whey: **22 g DE PROTEÍNA EM 30 g. 124 kcal. 30 DOSES.** O que não leva: açúcar adicionado em quantidade significativa. Adoçado com stevia e taumatina.
- Creatina: **UM INGREDIENTE. 3 g POR DOSE. A LISTA ACABA AQUI.**
- OnFire: **200 mg DE CAFEÍNA. CERCA DE DUAS XÍCARAS. NÃO DEPOIS DAS 17H.**
- Iso Whey: **22 g DE PROTEÍNA. 88 kcal. SEM AROMA E SEM ADOÇANTE.**
- Joints On: **1 CÁPSULA AO DIA. 30 DIAS.** (nada sobre efeito)

Páginas:
- Ciência: **O QUE OS ESTUDOS USARAM. O QUE O POTE ENTREGA. LADO A LADO.**
- Qualidade: **CADA POTE TEM UM LOTE. CADA LOTE FOI TESTADO.**
- Manifesto: **SUPLEMENTO BOM É O QUE VOCÊ CONSEGUE ENTENDER.** (frase real do site)
- Nutreon Pro: **PRESCREVA PELO RÓTULO. NÃO PELA COMISSÃO. AQUI NÃO TEM COMISSÃO.**
- Blog: títulos-pergunta com número: "VITAMINA D EVITA FRATURA SEM INDICAÇÃO?", "O TETO DE 1,62 g/kg/DIA É REAL?"

Microcopy: "Ver o rótulo inteiro", "Comprar", "Calcular frete", "Como testamos", "Quero me cadastrar". Aviso de topo em uma linha estática: "5% no Pix · 3x sem juros · Frete grátis acima de R$ 299 no Sul, Sudeste e Centro-Oeste". Rodapé: "Suplemento alimentar não é medicamento. Consulte um nutricionista." em tamanho de corpo.

Palavras proibidas: turbine, explosivo, queima, acelere, transforme seu corpo, eleve sua performance, fórmula exclusiva, blend proprietário, premium (como adjetivo), qualidade superior, nº 1, revolucionário, milagroso, garantido, resultado.

## 8. Arquitetura de páginas e o trabalho de cada uma

Menu: Loja por uso · Kits · Ciência · Qualidade · Nutreon Pro · Blog (Comunidade só com conteúdo autorizado). Mega menu de "Loja por uso" com as 6 categorias (Antes do treino · Recuperação e massa · Proteínas · Articulações · Base diária · Kits), um produto real e um número-chave em cada.

**Home** — provar em 60 segundos que a marca é diferente e levar ao produto em ≤ 3 cliques. Ordem: hero (título, sub, "Ver produtos", "Como testamos"; imagem real da shot list ou herói tipográfico, sem carrossel e sem o render do pote em destaque) → as cinco provas numeradas 01–05, cada uma com dado real → Loja por uso (6 cards tipográficos com produto) → "A página é o rótulo" (tabela real do Whey Chocolate com toggle Whey ↔ Iso Whey) → Ciência (4 ingredientes com barras "estudos vs. Nutreon") → Qualidade em seção laboratório → últimas análises do blog com selo de evidência → Pro → rodapé.

**Categoria** — comparar rápido. Cards com foto grande, nome, o número que decide ("22 g · 124 kcal"), "R$ 279" e "R$ 265,05 no Pix"; sem badge "Grátis", sem "-0% OFF". Esgotado aparece como esgotado.

**PDP** — vender sem esconder nada. Ordem: galeria real + título + preço + Pix + 3x sem juros + "Comprar" + frete recolhido → linha "Em 10 segundos" (22 g · 124 kcal · 30 doses · stevia + taumatina · contém lactose) → sumário lateral fixo → Composição por porção (tabela inteira, %VD) → Por que esta dose (lado a lado: ISSN 20–40 g por refeição vs. 22 g) → Modo de uso → Para quem e atenção → Ingredientes e alérgicos → O que não leva → Qualidade e rastreabilidade → Perguntas frequentes. Pagamento e parcelas num disclosure fechado. Disclaimer visível antes do fim.

**Ciência (hub + 4 ingredientes)** — hub com 4 cards grandes: ingrediente, faixa estudada, dose Nutreon, fonte. Página do ingrediente mantém a estrutura atual ("O que os estudos mostram" até "Revisado em"), com gráfico comparando faixa estudada e dose do produto.

**Blog (índice + post)** — levar o rigor dos cards para a web. Índice no padrão dos cards (pílula de tipo, título com highlight, selo de evidência). Post com a estrutura atual preservada ("Em 30 segundos", "O estudo em números" como tabela desenhada, forest plot em SVG, referências ABNT, caixa de transparência, download dos 6 cards), metadados em mono, sumário fixo.

**Qualidade** — hero em laboratório com a frase da seção 7; macro do lote impresso. Só o que a pergunta 1 permitir.

**Manifesto** — display gigante com a frase, três blocos numerados, "Nutreon, desde setembro de 2025".

**Nutreon Pro + Biblioteca** — convencer pela ética, não por vantagem. Hero, "O que o programa oferece", "Regras do programa" na íntegra, conflito de interesse em destaque, CTA para o cadastro externo, biblioteca com fichas e guia de ingredientes.

**Contato, Trocas e Devoluções, Privacidade** — mesmo sistema tipográfico, com sumário.

Redirecione: `/nosso-clean-label/` → Manifesto; `/nutreon-pro-laudo/` → Qualidade; `/lista-vip/` → 301 ou remoção; link do X corrigido ou removido.

## 9. Interações com propósito (e nenhuma a mais)

Cada interação prova algo ou economiza um gesto. Tudo respeita `prefers-reduced-motion`, nada passa de 600 ms, nada fica em loop.

- Highlight verde que "pinta" a palavra-chave da esquerda para a direita ao entrar na viewport, uma vez.
- Números-herói com contagem curta (≤ 500 ms), só para dados reais (22 g, 3 g, 200 mg, 25.871).
- Comparador "dose nos estudos vs. dose no pote": barras lado a lado, na PDP e em Ciência.
- Toggle Whey ↔ Iso Whey: mesma tabela; células que mudam ganham highlight.
- Calculadora de cafeína nas PDPs do OnFire e do Boost On: o usuário informa o peso, o site mostra mg/kg e a faixa estudada de 3 a 6 mg/kg (Guest et al., 2021), com os avisos do rótulo. Exemplo já publicado: 400 mg para 70 kg = cerca de 5,7 mg/kg.
- Sumário lateral fixo com scroll-spy na PDP e no post.
- Barra de evidência que preenche ao entrar; forest plot com tooltip do IC.
- Consulta por lote: só se o Gabriel confirmar na pergunta 1.

Proibido: parallax, scroll-jacking, cursor customizado, preloader, tilt 3D, partículas, marquee, carrossel automático, confete, som.

## 10. Plataforma: apresente, não decida

O e-commerce (carrinho, checkout, pagamento, frete, conta) é Nuvemshop e continua. Apresente em `porte/plano-nuvemshop.md`, com prós, contras, riscos, esforço e recomendação:

- **Rota A — tema Nuvemshop sob medida**: código próprio, zero herança do Toluca. Uma plataforma só; limitado pelo motor de temas (verifique se sumário fixo, toggle, calculadora e SVG no blog são viáveis).
- **Rota B — front-end headless** (Next.js ou Astro) para tudo que não é carrinho e checkout, lendo o catálogo da Nuvemshop; "Comprar" leva ao checkout Nuvemshop. Liberdade total; custo de manter dois ambientes e sincronizar estoque, preço e domínio.

Pergunte ao Gabriel. O protótipo estático vale para as duas.

## 11. Restrições legais e éticas (reprovam sozinhas)

- Disclaimer "Suplemento alimentar não é medicamento. Consulte um nutricionista." em toda página, legível.
- Só alegações do rótulo. A única funcional existente: "A cafeína contribui para o aumento do estado de alerta e da capacidade de resistência em exercícios físicos de resistência (alegação do rótulo)." Nada de cura, tratamento, emagrecimento, "queima", "imunidade".
- Avisos do rótulo preservados: cafeína (200 mg por dose; não somar OnFire e Boost On; gestantes, crianças, hipertensão; evitar depois das 17h), alérgicos, lactose.
- "Rigor de farmacopeia americana" é a frase. Não vira "certificado USP", "aprovado pela FDA" nem selo inventado.
- Sem antes e depois, depoimento, estrela sem avaliação real, contador de urgência, "mais de X clientes", prêmio.
- Nutreon Pro: sem comissão, pontuação, prêmio ou benefício ligado a compra de paciente; CREF não prescreve; CFN 856/2026, CFM e CONFEF citados; conflito de interesse do fundador visível. Vetadas: parceiro, embaixador, ganhe, indique.
- Blog: régua igual para favorável e desfavorável; caixa de transparência em todo post; referências ABNT; selo com "avaliação editorial" quando não for GRADE.
- Comunidade: só histórias com autorização por escrito. Sem conteúdo, sem página.
- Nenhum número fora do site ao vivo ou da fonte citada. Em dúvida, pergunte.

## 12. Critérios de aceite (todos obrigatórios)

1. Lighthouse mobile: Performance ≥ 90, Acessibilidade ≥ 95, SEO ≥ 95; LCP < 2,5 s; CLS < 0,1.
2. Contraste documentado: corpo e mono ≥ 4,5:1; display ≥ 3:1; nenhum texto `#12B693` sobre claro.
3. 390, 820 e 1440 px sem scroll horizontal; gutter ≥ 16 px no mobile; alvos de toque ≥ 44 px.
4. Zero lorem ipsum, zero placeholder, zero dado que não confira com o site ao vivo (anexe a conferência).
5. Home → "Comprar" do Whey Chocolate em ≤ 3 cliques; CTA do hero acima da dobra em 390 px.
6. PDP: tabela de composição a no máximo um scroll do CTA em 390 px; parcelas recolhidas; "O que não leva" e disclaimer presentes.
7. Tipografia: 2 famílias + 1 mono em tokens; display ≥ 72 px em 1440; nenhuma viúva em título de hero.
8. `grep -ri "labs\|NutreON"` retorna zero no protótipo e no copy deck.
9. Post: selo de evidência, "O estudo em números", forest plot, referências ABNT e caixa de transparência legíveis em 390 px.
10. Motion: tudo desliga com `prefers-reduced-motion`; nada > 600 ms; nada em loop.
11. Zero 404 interno; link do X resolvido; redirecionamentos listados.
12. Nenhum item da seção 13; checklist com screenshot por página e largura.
13. Copy deck com ao menos um título por página dentro da seção 7, enviado ao Gabriel.
14. Tudo acessível por teclado; foco visível.

## 13. Anti-padrões ("slop") que reprovam o trabalho

**Visual**: tudo da lista proibida da seção 6, mais gradiente roxo/azul; glassmorphism; cards com sombra enorme e raio de 24 px; trio de "features" centralizado; dark mode "matrix" com verde-neon em texto corrido; grid em contraste alto; todas as seções centralizadas com o mesmo espaçamento; Inter/Roboto em display; tudo em 400/700.

**Comercial**: pop-up na entrada; barra rolante; carrossel automático; badge "Grátis"; "-0% OFF"; 12 parcelas abertas; contador de urgência; estrelas sem avaliação; selo Nuvemshop em destaque; render de mockup como herói; selo "LHA" carimbado sobre foto.

**Copy**: palavra proibida da seção 7; exclamação; emoji institucional; pergunta retórica de venda; adjetivo sem número; texto justificado; aspas retas; "R$279" sem espaço; "LABS"/"NutreON".

**Técnico**: tudo da lista proibida da seção 9; animação sem `prefers-reduced-motion`; imagem sem `alt`; heading fora de ordem.

Um item em qualquer tela e o trabalho não está pronto.

## 14. Entregáveis

Em uma pasta do projeto, com `README.md`:

1. `auditoria.md` — preservar, reprovar, avaliação foto a foto.
2. `perguntas.md` — as 12 perguntas e as respostas.
3. `direcoes/` — 3 direções, recomendação, decisão de plataforma.
4. `prototipo/` — site estático com todas as páginas da seção 8 (PDPs ao menos de Whey Chocolate, OnFire Uva Verde e Creatina Monohidratada; post da proteína); screenshots nas 3 larguras.
5. `tokens/` — JSON e variáveis CSS: cor (com tabela de contraste), tipo, espaçamento, raio, sombra, motion.
6. `componentes/` — página-biblioteca: botões, pílulas, highlight, tabela nutricional, comparador de dose, barra de evidência, forest plot, cards, sumário fixo, disclosure, aviso de topo, rodapé, disclaimer.
7. `copy/copy-deck.md` — título, sub, CTAs e microcopy de cada página.
8. `fotografia/shot-list.md` e `fotografia/provisorias.md`.
9. `porte/plano-nuvemshop.md` — rota, passos, riscos, estimativa, manutenção.
10. `aceite/checklist.md` — os 14 critérios e os anti-padrões, marcados, com screenshot.

Você termina quando a equipe da seção 2 inteira aprovaria, o Gabriel reconheceria a Nutreon em cada tela e nenhum concorrente conseguiria usar o site trocando o logo. Precisão que dá tesão. Comece pela auditoria.
