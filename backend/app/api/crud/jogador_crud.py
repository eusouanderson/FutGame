from app.api.db.models import Jogador
from app.api.db import db

async def criar_jogador(jogador: Jogador):
    jogador_dict = jogador.dict()
    await db.jogadores.insert_one(jogador_dict)
    return jogador_dict

async def listar_jogadores():
    jogadores = []
    async for jogador in db.jogadores.find():
        jogadores.append(jogador)
    return jogadores
