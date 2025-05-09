from app.api.db.db import close_mongo_connection, connect_to_mongo
from app.api.routes.jogador_routes import router as jogador_router
from app.api.routes.webhook_routes import router as webhook_router
from fastapi import FastAPI

app = FastAPI()

print("http://localhost:8000/docs")


@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()


app.include_router(jogador_router, prefix="/jogadores", tags=["jogadores"])
app.include_router(webhook_router, prefix="/webhook", tags=["webhook"])


@app.get("/")
async def root():
    return {"message": "Server is running successfully!"}
