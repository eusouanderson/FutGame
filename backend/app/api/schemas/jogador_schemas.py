from pydantic import BaseModel

class Habilidades(BaseModel):
    força: int
    velocidade: int
    chute: int
    inteligencia: int
    técnica: int
    ataque: int
    defesa: int
    passe: int

class Jogador(BaseModel):
    nome: str
    idade: int
    habilidades: Habilidades
