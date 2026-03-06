from pydantic import BaseModel
from typing import Optional



class ServiceCreate(BaseModel):
    name: str
    category: str
    lat: float
    lon: float


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None



class ServiceResponse(BaseModel):
    id: int
    name: str
    category: str
    rating: Optional[float]

    class Config:
        from_attributes = True