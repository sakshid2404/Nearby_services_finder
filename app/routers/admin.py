from app.core.role_checker import require_roles
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
   

router = APIRouter(prefix="/admin")

@router.put("/assign-role/{user_id}")
def assign_role(
    user_id:int,
    role:str,
    db:Session=Depends(get_db),
    user=Depends(require_roles(["admin"]))
): 
    
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        return {"error":"user not found"}

    user.role=role
    db.commit()

    return {"message":"role assigned"}
    