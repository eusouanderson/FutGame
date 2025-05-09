from app.api.db.db import criar_jogador, listar_jogadores
from app.api.schemas.jogador_schemas import Jogador
from fastapi import APIRouter

router = APIRouter()


@router.post("/criar_jogador")
async def criar_jogador_route(jogador: Jogador):
    jogador_criado = await criar_jogador(jogador)
    return {"message": "Jogador criado com sucesso!", "jogador": jogador_criado}


@router.get("/listar_jogadores")
async def listar_jogadores_route():
    try:
        jogadores = await listar_jogadores()
        return {"jogadores": jogadores}
    except Exception as e:
        return {"error": str(e)}
