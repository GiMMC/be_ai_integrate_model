from fastapi import APIRouter, Depends
from app.api.v1.deps import get_current_user
from app.services.ai_service import generate_text

router = APIRouter()

@router.post("/generate")
async def generate(prompt: str, user=Depends(get_current_user)):
    result = await generate_text(prompt)
    return result