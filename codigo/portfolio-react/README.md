# Portfólio — React e TypeScript

Fonte da interface do portfólio de Jhonata Selmo. Componentes TSX, estilos CSS e script JavaScript de geração estática.

## Gerar HTML

Requer Node.js 22.13 ou superior.

```sh
npm install
npm run build
python3 -m http.server 8080 --directory dist
```

Abra http://localhost:8080. O build gera `dist/index.html` a partir de `app/page.tsx`.
