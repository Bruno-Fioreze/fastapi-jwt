from lib2to3.pytree import Base
from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str