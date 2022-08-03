from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Text
from src.settings.database import meta, engine

InstagramPublicationsModel = Table(
    "new_post", meta, 
    Column("SHORTCODE", String(255), primary_key=True),
    Column("TITLE", Text),
    Column("OWNER_USERNAME", String(255)),
    Column("OWNER_ID", Integer),
    Column("LOCAL_DATE", DateTime),
    Column("CAPTION", Text),
    Column("CAPTION_HASHTAGS", String(255)),
    Column("CAPTIONS_MENTIONS", String(255)),
    Column("URL", String(255)),
    Column("TYPENAME", String(255)),
    Column("TAGGED_USERS", String(255)),
    Column("VIDEO_URL", String(255)),
    Column("VIDEO_VIEW_COUNT", Integer),
    Column("VIDEO_DURATION", String(255)),
    Column("LIKES", Integer),
    Column("COMMENTS", Integer),
    Column("date_create", DateTime, default=datetime.utcnow())
)

meta.create_all(engine)