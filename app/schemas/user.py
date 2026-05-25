from pydantic import BaseModel, EmailStr
from pydantic_br import CPF
from typing import Optional

class AuthUserCreate(BaseModel):
    username: str
    email: EmailStr
    register: CPF
    password: str

class AuthUserResponse(BaseModel):
    id: int
    username: str
    email: str
    register: str
    status: bool

    class Config:
        from_attributes = True

class AuthToken(BaseModel):
    token: str
    type: str

class AuthTokenData(BaseModel):
    username: Optional[str] = None
    