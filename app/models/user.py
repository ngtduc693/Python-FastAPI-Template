from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: str
    full_name: str
    phone: str
    email: EmailStr
    two_fa_enabled: bool = False
    gender: Optional[str] = None
    country: Optional[str] = None
    preferred_language: Optional[str] = None
