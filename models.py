from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
# from .database import Base
from database import Base


class CollectionItem(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String, index=True)  
    status = Column(String, default="Pendiente")
    rating = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())