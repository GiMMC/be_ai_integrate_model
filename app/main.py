from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="API V1 Integrations",
    description="Model Chatgpt API Integrations",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")