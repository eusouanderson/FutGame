from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

async def connect_to_mongo(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
    app.db = app.mongodb_client.jogador
    print("Conectado ao MongoDB!")

async def close_mongo_connection(app: FastAPI):
    app.mongodb_client.close()
    print("Conexão com MongoDB fechada!")
