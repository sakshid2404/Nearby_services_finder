from sqlalchemy import Column, Integer, String, Float, DateTime
from geoalchemy2 import Geography
from datetime import datetime

from app.database import Base


class Service(Base):

    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    rating = Column(Float, nullable=True)

    location = Column(
        Geography(geometry_type="POINT", srid=4326),
        nullable=False
    )

    created_at = Column(DateTime, default=datetime.utcnow)