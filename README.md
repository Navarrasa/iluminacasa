# 🛋️ IluminaCasa

> **IluminaCasa** é uma loja online dedicada à venda de **móveis, utensílios domésticos e acessórios com** 
> **iluminação personalizada**, trazendo aconchego, praticidade e estilo para seu lar.

## ✨ Visão Geral

Este repositório é um monorepo contendo o **frontend** (com Next.js) e o **backend** (com FastAPI) da aplicação IluminaCasa.

A arquitetura foi pensada para ser escalável, modular e com separação clara de responsabilidades, facilitando a manutenção e colaboração.

## 🧱 Tecnologias Utilizadas

### 🖥️ Frontend

- Next.js – Framework React com renderização híbrida (SSG/SSR)
- TypeScript – Tipagem estática
- PNPM – Gerenciador de pacotes moderno
- React Hooks – Para controle de estado e efeitos
- CSS Modules / TailwindCSS – Para a estilização da aplicação

### 🔌 Backend

- FastAPI – Framework web moderno em Python
- uvicorn – Servidor ASGI de alto desempenho
- Pydantic – Validação e tipagem de dados
- uv – Gerenciador de dependências super rápido (alternativa ao pip)

## 📁 Estrutura do Projeto

```
tree

iluminacasa/
├── frontend/              # Projeto Next.js
│   └── src/
│       └── app/
│           ├── pages/            # Páginas da aplicação
│           ├── ui/               # Componentes reutilizáveis
│           │   ├── Button/
│           │   └── Card/
│           ├── hooks/            # Hooks customizados
│           ├── lib/
│           │   ├── services/     # Comunicação com API
│           │   │   ├── userApi.ts
│           │   │   └── productApi.ts
│           │   └── utils/        # Funções utilitárias
│           ├── styles/           # Estilos globais
│           ├── config/           # Configurações gerais
│           └── features/         # Funcionalidades por domínio
│               ├── user/
│               └── product/
│
├── iluminacasa_backend/    # Projeto FastAPI
│   ├── app/
│   │   ├── api/            # Rotas
│   │   ├── models/         # Modelos do banco de dados
│   │   ├── schemas/        # Esquemas Pydantic
│   │   ├── services/       # Lógica de negócio
│   │   └── main.py         # Ponto de entrada FastAPI
│   ├── requirements.txt    # Dependências
│   └── .env                # Variáveis de ambiente
│
├── README.md
└── .gitignore
```

## ⚙️ Como rodar localmente

### 📦 Pré-requisitos

- Node.js (v18+)
- Python (3.10+)
- PNPM – para o frontend
- uv – para o backend (alternativa ao pip)

## 🔧 Instalação

```
bash

# Clone o repositório
git clone https://github.com/Navarrasa/IluminaCasa.git
cd iluminacasa
```

#### Frontend (Next.js)
```
bash

cd frontend
pnpm install
pnpm dev
```

#### Backend (FastAPI)
```
bash

cd ../iluminacasa_backend
uv pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🚀 Rotas e Endpoints

### Frontend

- / – Página inicial
- /produtos – Catálogo
- /produtos/[id] – Detalhe de produto
- /login, /carrinho, etc.

### Backend (API)

- GET /products – Lista de produtos
- GET /products/{id} – Produto por ID
- POST /auth/login – Login de usuário

## 📌 Roadmap

- [x] Estrutura inicial com monorepo
- [x] Setup do Next.js e FastAPI
- [ ] Catálogo de produtos
- [ ] Carrinho e checkout
- [ ] Autenticação de usuários
- [ ] Integração com gateway de pagamento
- [ ] Deploy (Vercel + Render/Fly.io)

## 📝 Licença

MIT © **devBruno - 2025**