from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    """Schema for creating a user."""
    full_name: str = Field(..., min_length=1, max_length=100)
    phone: str = Field(..., min_length=8, max_length=20)
    email: EmailStr
    two_fa_enabled: bool = False
    gender: Optional[str] = Field(None, description="Male, Female, Other")
    country: Optional[str] = None
    preferred_language: Optional[str] = None

class UserRead(UserCreate):
    """Schema for reading a user (with id)."""
    id: str
