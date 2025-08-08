from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# SlowAPI
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

# middleware.py
"""
Propósito: Definir middlewares para a aplicação FastAPI — interceptadores que atuam antes/depois das rotas.

-> Configurar CORS, definindo domínios liberados.
-> Configurar rate limiting (ex: SlowAPI).
-> Middleware para logging de requisições e respostas.
-> Middleware para captura global de exceções e alertas (e.g. enviar email/Slack se falhar).
-> Qualquer outra função que precise “envelopar” as requisições/respostas.

"""


def configure_middleware(app):
    """
    Configure the FastAPI application with various middlewares.

    This function sets up the application with the following middlewares:

    - SlowAPIMiddleware: A middleware to handle rate limiting.
    - GZipMiddleware: A middleware to compress responses larger than 1000 bytes.
    - CORSMiddleware: A middleware to enable CORS on the application.

    :param app: The FastAPI application instance.
    """

    app.add_exception_handler(RateLimitExceeded)
    app.add_middleware(SlowAPIMiddleware)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["localhost", "127.0.0.1", "http://localhost:3000"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )