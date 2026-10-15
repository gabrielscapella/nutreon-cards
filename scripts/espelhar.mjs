// Espelha os cards do blog Nutreon Ciência (já públicos no CDN do blog) neste repositório público,
// servido pelo jsDelivr com CORS, para o botão "Postar no Instagram" anexar as imagens no celular.
// Lê o sitemap do blog, abre cada post e baixa as imagens listadas em data-nt-cards. Sem chave: só leitura pública.
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
const UA = { 'User-Agent': 'Mozilla/5.0 (Nutreon Ciencia; espelho de cards)' };
const sitemap = await (await fetch('https://www.nutreon.com.br/sitemap_blog.xml', { headers: UA })).text();
const indice = await (await fetch('https://www.nutreon.com.br/blog/', { headers: UA })).text();
// o sitemap demora a atualizar: soma os posts listados na página do blog
const posts = [...new Set([
  ...[...sitemap.matchAll(/<loc>([^<]+\/blog\/posts\/[^<]+)<\/loc>/g)].map(m => m[1]),
  ...[...indice.matchAll(/href="((?:https:\/\/www\.nutreon\.com\.br)?\/blog\/posts\/[\w-]+)\/?"/g)].map(m => m[1].startsWith('http') ? m[1] : 'https://www.nutreon.com.br' + m[1]),
])];
mkdirSync('m', { recursive: true });
let novos = 0;
for (const url of posts) {
  const html = await (await fetch(url, { headers: UA })).text();
  const lista = html.match(/data-nt-cards="([^"]+)"/)?.[1].split(/\s+/).filter(u => /^https:\/\/cdn-blog-backend\.tiendanube\.com\//.test(u)) ?? [];
  for (const u of lista) {
    const nome = u.split('/').pop();
    if (!/^[\w-]+\.(jpg|jpeg|png)$/i.test(nome) || existsSync(`m/${nome}`)) continue;
    const r = await fetch(u, { headers: UA });
    if (!r.ok) { console.log(`falhou ${u}: HTTP ${r.status}`); continue; }
    writeFileSync(`m/${nome}`, Buffer.from(await r.arrayBuffer()));
    novos++; console.log(`novo: ${nome} (${url})`);
  }
}
console.log(`${posts.length} posts lidos, ${novos} cards novos`);
