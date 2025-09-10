from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# middleware.py
"""
Propósito: Definir middlewares para a aplicação FastAPI — interceptadores que atuam antes/depois das rotas.

-> Configurar CORS, definindo domínios liberados.
-> Configurar rate limiting (ex: SlowAPI).
-> Qualquer outra função que precise “envelopar” as requisições/respostas.

"""

limiter = Limiter(key_func=get_remote_address)

def _rate_limit_exceeded_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"},
    )

def configure_middleware(app):
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(SlowAPIMiddleware)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
