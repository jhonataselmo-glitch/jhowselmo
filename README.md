# Radar TI

Painel privado para localizar e acompanhar vagas de tecnologia compatíveis com o perfil profissional de Jhonata Selmo.

## Recursos

- Busca vagas remotas destinadas ao Brasil.
- Filtros de publicação: últimas 24 horas, 1 semana ou 1 mês.
- Ranking de aderência por cargo, competências, senioridade e experiência.
- Filtro especial para empresas de Educação e EdTech.
- Indicador de empresas com vagas compatíveis recorrentes.
- Priorização do link específico da candidatura quando disponível.
- Kanban para acompanhar candidatura, triagem, entrevista e oferta.
- Comparação de competências exigidas com o perfil profissional.
- Dados do painel salvos localmente no navegador.

## Tecnologias

- Next.js 16
- React 19
- Vinext
- Cloudflare Workers

## Executar localmente

Requisitos: Node.js 20 ou superior e npm.

```bash
npm install
npm run dev
```

Acesse `http://localhost:3000`.

Para testar o build de produção:

```bash
npm run build
npm run start
```

## Fontes de vagas

O endpoint `app/api/jobs/route.js` consulta fontes públicas e normaliza os resultados. O sistema não envia nome, telefone, e-mail ou currículo para essas fontes; utiliza apenas termos profissionais genéricos.

As fontes podem alterar limites, formato ou disponibilidade. Quando uma consulta falha, o painel informa a indisponibilidade em vez de afirmar que não existem vagas.

## Publicar no GitHub

Depois de extrair o ZIP, abra a pasta no terminal e execute:

```bash
git init
git add .
git commit -m "Publica Radar TI"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/radar-ti.git
git push -u origin main
```

Crie antes um repositório vazio chamado `radar-ti` na sua conta do GitHub e substitua `SEU-USUARIO` pelo seu usuário.

## Privacidade

Não adicione currículos, senhas, tokens ou arquivos `.env` ao repositório público. O pacote distribuído não contém o currículo usado na análise, dados de contato, pasta de build, dependências instaladas ou histórico Git interno.
