from sqlalchemy import Column, Integer, String, Float
from geoalchemy2 import Geography
from app.database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Service(Base):

    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    rating = Column(Float, nullable=True)

    location = Column(
        Geography(geometry_type="POINT", srid=4326)
    )
    created_at = Column(DateTime, default=datetime.utcnow)