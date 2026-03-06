from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(username:str,email:str,password:str,db:Session=Depends(get_db)):

    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()

    return {"message":"user created"}

@router.post("/login")
def login(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token(
        data={"sub": user.username}   # VERY IMPORTANT
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }