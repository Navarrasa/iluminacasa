from schemas.auth import LoginSchema, RegisterSchema

async def userLogin(login_data: LoginSchema):

    # Lógica

    return {
            "message": "Logged in succesfully!",
            "token": token,
            }

async def userRegister(register_data: RegisterSchema):
    
    # Lógica
    
    return register_data

async def userLogout():
    
    # Lógica
    
    return {"message": "logged out!"}
