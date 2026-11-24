# Tecnologias e evidências

Este índice liga as tecnologias apresentadas no portfólio aos arquivos públicos. A barra de linguagens do GitHub mede bytes de código; ela não é uma avaliação de proficiência profissional.

| Tecnologia | Evidência no repositório |
| --- | --- |
| Python | [NORT Desktop AI](../codigo/nort-desktop-ai/nort/) e [AWS Bedrock Assistant](../codigo/aws-bedrock-assistant/assistant.py) |
| TypeScript / React | [Página do portfólio em TSX](../codigo/portfolio-react/app/page.tsx) |
| JavaScript | [Build estático em módulos ES](../codigo/portfolio-react/scripts/build-static.mjs) |
| CSS | [Estilos fonte](../codigo/portfolio-react/app/globals.css) |
| PowerShell | [Script de build do instalador Windows](../codigo/nort-desktop-ai/installer/build.ps1) |
| HTML | [Página estática gerada](../portfolio/index.html); excluída das estatísticas como saída de build |
| AWS / IA generativa | [Cliente Amazon Bedrock, testes offline e política IAM de exemplo](../codigo/aws-bedrock-assistant/) |

## Habilidades com outro escopo

**SQL** aparece na experiência de dados e nos projetos com persistência SQL apresentados no portfólio; não há arquivos SQL publicados aqui. **Power BI, Excel, Microsoft 365, Google Workspace, IAM e LGPD** são ferramentas ou áreas de atuação, não linguagens a acrescentar à barra automática.

## Executar a demonstração AWS sem cobranças

```sh
cd codigo/aws-bedrock-assistant
python3 -m unittest discover -s tests -v
```

Os testes usam um cliente simulado. Executar a integração real com Bedrock exige conta, credenciais, permissões e modelo compatível e pode gerar cobranças.

## Ler os projetos

- [Apura.IA](../projetos/apura-ia.md)
- [JS Labs](../projetos/js-labs.md)
- [NORT Desktop: arquitetura](../codigo/nort-desktop-ai/ARCHITECTURE.md)
- [NORT Desktop: validação e limites](../codigo/nort-desktop-ai/VALIDATION.md)
- [Portfólio React: build](../codigo/portfolio-react/README.md)
