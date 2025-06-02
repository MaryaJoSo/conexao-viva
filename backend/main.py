from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import User, UserLogin, Message
from database import fake_users_db, fake_messages_db
from auth import hash_password, verify_password, create_access_token, decode_access_token
from datetime import timedelta

app = FastAPI()

# Configurar CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas de autenticação e mensageria

@app.post("/register")
def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    hashed_password = hash_password(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "anonymous": user.anonymous
    }
    return {"msg": "Usuário registrado com sucesso"}

@app.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(authorization: str = Header(...)):
    token = authorization.split(" ")[1] if " " in authorization else authorization
    username = decode_access_token(token)
    if username is None or username not in fake_users_db:
        raise HTTPException(status_code=401, detail="Token inválido")
    return username

@app.post("/messages")
def send_message(message: Message, current_user: str = Depends(get_current_user)):
    msg = {
        "sender": current_user,
        "receiver": message.receiver,
        "content": message.content
    }
    fake_messages_db.append(msg)
    return {"msg": "Mensagem enviada com sucesso"}

@app.get("/messages", response_model=List[Message])
def read_messages(current_user: str = Depends(get_current_user)):
    user_msgs = [
        Message(**msg) for msg in fake_messages_db if msg["receiver"] == current_user
    ]
    return user_msgs

@app.get("/api")
def root():
    return {"message": "API do Conexão Viva funcionando"}