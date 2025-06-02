from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: Optional[str] = None
    password: str
    anonymous: bool = False

class UserLogin(BaseModel):
    username: str
    password: str

class Message(BaseModel):
    sender: str
    receiver: str
    content: str