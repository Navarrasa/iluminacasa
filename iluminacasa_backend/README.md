# Project Tree IluminaCasa

### Uma "Árvore Genealógica" do projeto, que demonstra todas as rotas e explica resumidamente a função de cada arquivo ou pasta.

iluminacasa_backend/
│
├─ app/
│  ├─ api/
│  │  └─ v1/
│  │     ├─ api.py           # Router principal que junta todos os endpoints da API v1
│  │     ├─ auth.py          # Endpoints de autenticação (login, registro)
│  │     ├─ cart.py          # Endpoints do carrinho de compras
│  │     ├─ orders.py        # Endpoints de pedidos
│  │     ├─ product.py       # Endpoints de produtos
│  │     └─ users.py         # Endpoints de usuários
│  │
│  ├─ core/
│  │  ├─ config.py           # Configurações gerais da aplicação (variáveis de ambiente, CORS, etc)
│  │  ├─ middleware.py       # Middlewares (CORS, rate limiting, etc)
│  │  ├─ security.py         # Funções de segurança (hashing, tokens JWT, etc)
│  │  └─ database/
│  │     ├─ database.py      # Configuração do banco de dados e sessão
│  │     └─ models/          # Modelos ORM divididos por domínio (auth, cart, orders, user)
│  │
│  ├─ dependencies.py        # Dependências FastAPI (ex: sessão do banco, usuário atual)
│  ├─ main.py                # Inicialização do app FastAPI, inclusão dos routers e middlewares
│  ├─ schemas/               # Schemas Pydantic para validação e serialização de dados (auth, products)
│  └─ services/              # Lógica de negócio e serviços externos (ex: auth_service.py, dummyjson.py)
│
└─ database.db               # Banco de dados SQLite local (se aplicável)
