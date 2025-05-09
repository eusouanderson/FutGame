import os
from typing import Dict

from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

client: AsyncIOMotorClient = None
database = None
jogadores_collection = None

env = os.getenv("ENVIRONMENT", "development")

if env == "production":
    mongo_uri = "mongodb://mongo:27017"
else:
    mongo_uri = "mongodb://192.168.15.7:27017"


async def connect_to_mongo():
    global client, database, jogadores_collection
    try:
        uri = mongo_uri
        print(f"Conectando ao MongoDB na URI: {uri}")
        client = AsyncIOMotorClient(uri)

        await client.server_info()

        database = client.get_database("jogador")
        jogadores_collection = database.get_collection("jogadores")
        print("✅ Conectado ao MongoDB!")

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        client = None
        jogadores_collection = None


async def close_mongo_connection():
    if client:
        try:
            await client.close()
            print("🛑 Conexão com MongoDB fechada!")
        except Exception as e:
            print(f"Erro ao fechar a conexão com o MongoDB: {e}")
    else:
        print("Não há conexão ativa com o MongoDB.")


def init_db(app: FastAPI):
    @app.on_event("startup")
    async def startup_db():
        await connect_to_mongo()

    @app.on_event("shutdown")
    async def shutdown_db():
        await close_mongo_connection()


async def criar_jogador(jogador_dict: Dict):
    if jogadores_collection is None:
        raise HTTPException(
            status_code=500, detail="Conexão com o MongoDB não estabelecida."
        )

    try:
        if isinstance(jogador_dict, BaseModel):
            jogador_dict = jogador_dict.dict()
        result = await jogadores_collection.insert_one(jogador_dict)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        print(f"Erro ao inserir jogador: {e}")
        raise HTTPException(status_code=500, detail="Erro ao inserir jogador.")


async def listar_jogadores():
    if jogadores_collection is None:
        raise HTTPException(
            status_code=500, detail="Conexão com o MongoDB não estabelecida."
        )

    try:
        jogadores_cursor = jogadores_collection.find()
        jogadores = await jogadores_cursor.to_list(length=None)
        for jogador in jogadores:
            jogador["_id"] = str(jogador["_id"])

        return jogadores
    except Exception as e:
        print(f"Erro ao listar jogadores: {e}")
        raise HTTPException(status_code=500, detail="Erro ao listar jogadores.")
