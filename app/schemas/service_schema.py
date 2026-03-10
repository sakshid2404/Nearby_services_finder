from pydantic import BaseModel, Field
from typing import Optional


class ServiceCreate(BaseModel):

    name: str = Field(..., example="City Hospital")

    category: str = Field(..., example="hospital")

    latitude: float = Field(..., example=19.9975)

    longitude: float = Field(..., example=73.7898)


class ServiceUpdate(BaseModel):

    name: Optional[str] = None

    category: Optional[str] = None

    rating: Optional[float] = None


class ServiceResponse(BaseModel):

    id: int
    name: str
    category: str
    rating: Optional[float]

    class Config:
        from_attributes = True


class NearbyServiceResponse(BaseModel):

    id: int
    name: str
    category: str
    rating: Optional[float]
    distance_km: float