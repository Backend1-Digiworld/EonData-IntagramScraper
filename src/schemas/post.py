from typing import Optional
from pydantic import BaseModel 
from datetime import datetime

class InstagramPublications(BaseModel):
    SHORTCODE: str
    TITLE: str
    OWNER_USERNAME: str
    OWNER_ID: int
    LOCAL_DATE: datetime
    CAPTION: str
    CAPTION_HASHTAGS: str
    CAPTIONS_MENTIONS: str
    URL: str
    TYPENAME: str
    TAGGED_USERS: str
    VIDEO_URL: str
    VIDEO_VIEW_COUNT: int
    VIDEO_DURATION: str
    LIKES: int
    COMMENTS: int
    date_create: datetime