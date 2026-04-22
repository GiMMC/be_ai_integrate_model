from fastapi import APIRouter
from app.api.v1.endpoints import auth, ai

router = APIRouter()
router.include_router(auth.router, prefix="/auth")
router.include_router(ai.router, prefix="/ai")