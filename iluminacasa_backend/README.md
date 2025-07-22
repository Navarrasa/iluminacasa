```
IluminaCasa
├─ iluminacasa_backend
│  ├─ .python-version
│  ├─ app
│  │  ├─ api
│  │  │  └─ v1
│  │  │     ├─ api.py       # Endpoint de Rotas da API
│  │  │     ├─ auth.py      # Endpoint de Autenticação
│  │  │     ├─ cart.py      # Endpoint de Carrinho de Compras
│  │  │     ├─ login.py     # Endpoint de Login/Logout
│  │  │     ├─ orders.py    # Endpoint de Ordens de Compra
│  │  │     ├─ product.py   # Endpoint de Produtos
│  │  │     └─ users.py     # Endpoint de Usuários
│  │  ├─ core               # Configurações centrais (ex: settings, logging, exceptions)
│  │  │  └─ main.py
│  │  ├─ dependencies.py    # Injeção de dependências (ex: Auth, DB, API Clients)
│  │  ├─ main.py            # Criação do app, inclusão de rotas
│  │  ├─ models             # Schemas (Pydantic), modelos ORM se usar SQLAlchemy
│  │  │  └─ main.py
│  │  ├─ services           # Lógica de negócio (ex: chamada à DummyJSON)
│  │  │  ├─ auth
│  │  │  │  └─ auth_service.py
│  │  │  └─ dummyjson.py
│  │  └─ utils              # Funções auxiliares
│  ├─ pyproject.toml
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ tests                 # Testes unitários e de integração
│  │  └─ test_products.py
│  └─ uv.lock
```