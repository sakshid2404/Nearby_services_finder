from fastapi import Depends
from fastapi.security import HTTPBearer
from jose import jwt
from app.core.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_user(token = Depends(security)):

    payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])

    return payload