from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, Anderson! Bem-vindo à sua API FastAPI"}
