from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional, Literal

class ItemCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = ""
    category: Optional[str] = "GENERAL"
    status: Literal["Pendiente", "En Progreso", "Completado"]
    rating: float = 0.0

class ItemResponse(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: Optional[str]
    category: Optional[str]
    status: Literal["Pendiente", "En Progreso", "Completado"]
    rating: float
    created_at: datetime

    class Config:
        from_attributes = True

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)

    @field_validator("status")
    @classmethod
    def validate_status(cls, v):
        allowed_statuses = {"Pendiente", "En Progreso", "Completado"}
        if v is not None and v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v