from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(
    title="Credentia",
    version="0.0.1",
)

app.include_router(router)