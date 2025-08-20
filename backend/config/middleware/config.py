from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

# middleware.py
"""
Propósito: Definir middlewares para a aplicação FastAPI — interceptadores que atuam antes/depois das rotas.

-> Configurar CORS, definindo domínios liberados.
-> Configurar rate limiting (ex: SlowAPI).
-> Qualquer outra função que precise “envelopar” as requisições/respostas.

"""

def configure_middleware(app):

    app.add_exception_handler(RateLimitExceeded)
    app.add_middleware(SlowAPIMiddleware)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )