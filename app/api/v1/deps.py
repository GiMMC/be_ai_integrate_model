from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.core.security import verify_token

security = HTTPBearer()

def get_current_user(credentials=Depends(security)):
    try:
        payload = verify_token(credentials.credentials)
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")