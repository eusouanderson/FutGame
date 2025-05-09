~~
.
├── app/
│ ├── **init**.py
│ ├── api/
│ │ ├── **init**.py
│ │ ├── crud/
│ │ │ ├── **init**.py
│ │ │ └── jogador_crud.py
│ │ ├── db/
│ │ │ ├── **init**.py
│ │ │ ├── db.py
│ │ │ └── models.py
│ │ ├── routes/
│ │ │ ├── **init**.py
│ │ │ ├── jogador_routes.py
│ │ │ └── other_routes.py # Caso tenha outras rotas
│ │ ├── schemas/
│ │ │ ├── **init**.py
│ │ │ └── jogador_schemas.py
│ │ └── main.py # Arquivo principal da API
│ ├── config/
│ │ ├── **init**.py
│ │ ├── settings.py # Configurações gerais do app
│ │ └── logger.py # Se precisar de logging personalizado
│ └── tests/
│ ├── **init**.py
│ ├── test_jogadores.py # Testes relacionados aos jogadores
│ └── test_db.py # Testes de conexão com o banco
└── requirements.txt # Dependências do projeto
~~

db.jogadores.deleteMany({})

db.jogadores.find().pretty()

docker-compose down --volumes --remove-orphans
docker system prune -f
docker-compose build --no-cahe
docker-compose up
