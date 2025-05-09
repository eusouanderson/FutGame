from fastapi import FastAPI
from app.api.routes.webhook_routes import router as webhook_router
from app.api.db.db import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo(app)

@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection(app)

app.include_router(webhook_router, prefix="/webhook", tags=["webhook"])

@app.get("/")
async def root():
    return {"message": "Server is running successfully!"}
