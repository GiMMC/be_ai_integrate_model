from fastapi import APIRouter, Depends
from app.api.v1.deps import get_current_user
from app.services.ai_service import generate_text
from app.schemas.ai import AIRequest

router = APIRouter()

@router.post("/generate")
async def generate(data: AIRequest, user=Depends(get_current_user)):
    result = await generate_text(data.model, data.prompt)
    return result