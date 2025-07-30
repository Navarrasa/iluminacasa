from slowapi import Limiter
from slowapi.util import get_remote_address
from main import app
from fastapi.middleware.cors import CORSMiddleware

limiter = Limiter(key_func=get_remote_address)

def setup_rate_limit(app):
    app.state.limiter = limiter
    app.add_exception_handler(429, limiter._rate_limit_exceeded_handler)


def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # ou lista de domínios autorizados
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
A