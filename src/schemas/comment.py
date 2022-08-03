from typing import Optional
from datetime import datetime

from pydantic import BaseModel 

class InstagramComment(BaseModel):
    POST: str
    TYPE: str
    ID: int
    DATE: datetime
    TEXT: str
    OWNER_ID: int
    OWNER_USERNAME: str
    LIKES: int
    date_create: datetime