
# middleware.py
"""
Propósito: Definir middlewares para a aplicação FastAPI — interceptadores que atuam antes/depois das rotas.

-> Configurar CORS, definindo domínios liberados.
-> Configurar rate limiting (ex: SlowAPI).
-> Middleware para logging de requisições e respostas.
-> Middleware para captura global de exceções e alertas (e.g. enviar email/Slack se falhar).
-> Qualquer outra função que precise “envelopar” as requisições/respostas.

"""
