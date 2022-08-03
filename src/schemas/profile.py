from typing import Optional
from pydantic import BaseModel 
from datetime import datetime

class InstagramUser(BaseModel):
    pk: str
    username: str
    full_name: str
    profile_pic_url: str 
    biography: str
    external_url: str 
    follows_count: int
    followed_by_count: int 
    media_count: int
    is_private: bool  
    is_verified: bool
    id: int  
    is_active: bool
    date_create: datetime