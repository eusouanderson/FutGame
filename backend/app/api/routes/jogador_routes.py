from fastapi import APIRouter, Depends
from app.api.schemas.jogador_schemas import Jogador
from app.api.crud.jogador_crud import criar_jogador, listar_jogadores

router = APIRouter()

@router.post("/criar_jogador")
async def criar_jogador_route(jogador: Jogador):
    jogador_criado = await criar_jogador(jogador)
    return {"message": "Jogador criado com sucesso!", "jogador": jogador_criado}

@router.get("/listar_jogadores")
async def listar_jogadores_route():
    jogadores = await listar_jogadores()
    return jogadores
