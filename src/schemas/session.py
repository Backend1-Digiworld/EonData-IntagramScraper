from typing import Optional
from datetime import datetime

from pydantic import BaseModel 

class InstagramAcount(BaseModel):
    username: str
    password: str
    last_used: datetime
    available:  bool
    email: str
    phone: int
    is_used: bool
    is_dead: bool