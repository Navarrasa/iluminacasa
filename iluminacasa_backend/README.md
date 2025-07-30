```
- Documentação geral da estrutura do projeto iluminacasa_backend.

Este projeto é uma aplicação FastAPI organizada de forma modular e escalável, com as seguintes responsabilidades:

- app/api/v1/
    Contém os roteadores da API versão 1, organizados por domínio funcional:
    - api.py: roteador principal que agrega os sub-roteadores (auth, cart, orders, product, users).
    - auth.py, cart.py, orders.py, product.py, users.py: definem as rotas específicas e tratam as requisições para cada domínio.

- app/config/
    Configurações globais e infraestrutura da aplicação:
    - settings.py: gerenciamento e carregamento das variáveis de ambiente via Pydantic.
    - database/: inicialização da conexão com o banco de dados e definição dos modelos (tabelas) usando SQLModel.
    - handlers/: configuração de handlers globais, como loggers e tratamento centralizado de exceções.
    - middleware/: definição e registro dos middlewares globais, como CORS e rate limiting.

- app/database.db
    Arquivo de banco de dados SQLite (desenvolvimento).

- app/dependencies.py
    Define dependências reutilizáveis para as rotas, como autenticação, permissões e sessão de banco.

- app/schemas/
    Modelos Pydantic para validação e serialização de dados de entrada e saída, organizados por domínio (ex: auth.py, products.py).

- app/services/
    Camada de serviço contendo a lógica de negócio:
    - auth/: serviços de autenticação (login, token, logout).
    - dummyjson.py: integração com APIs externas para dados fictícios, por exemplo.

Esta organização facilita a manutenção, escalabilidade e legibilidade do código, separando claramente a lógica de negócio, rotas, configurações, e modelos.

Árvore de diretórios principal do projeto:

iluminacasa_backend/
│
├─ app/
│  ├─ api/
│  │  └─ v1/
│  │     ├─ api.py
│  │     ├─ auth.py
│  │     ├─ cart.py
│  │     ├─ orders.py
│  │     ├─ product.py
│  │     └─ users.py
│  ├─ config/
│  │  ├─ database/
│  │  │  ├─ database.py
│  │  │  └─ models/
│  │  │     ├─ auth.py
│  │  │     ├─ cart.py
│  │  │     ├─ orders.py
│  │  │     └─ user.py
│  │  ├─ handlers/
│  │  │  └─ config.py
│  │  ├─ middleware/
│  │  │  └─ config.py
│  │  └─ settings.py
│  ├─ database.db
│  ├─ dependencies.py
│  ├─ main.py
│  ├─ schemas/
│  │  ├─ auth.py
│  │  └─ products.py
│  └─ services/
│     ├─ auth/
│     │  └─ auth_service.py
│     └─ dummyjson.py
"""
```