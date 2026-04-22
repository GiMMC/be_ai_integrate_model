from fastapi import APIRouter
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login():
    # dummy user
    token = create_access_token({"user_id": "123"})
    return {"access_token": token}