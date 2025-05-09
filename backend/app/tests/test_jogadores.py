from app.api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_criar_jogador():
    response = client.post(
        "/jogadores/criar_jogador",
        json={
            "nome": "Jogador Teste",
            "idade": 25,
            "habilidades": {
                "força": 80,
                "velocidade": 75,
                "chute": 90,
                "inteligencia": 85,
                "técnica": 88,
                "ataque": 92,
                "defesa": 75,
                "passe": 80,
            },
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Jogador criado com sucesso!",
        "jogador": response.json()["jogador"],
    }


def test_listar_jogadores():
    response = client.get("/jogadores/listar_jogadores")
    assert response.status_code == 200
