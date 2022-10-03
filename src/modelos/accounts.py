from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Text
from src.settings.database import meta, engine
    
InstagramUserModel = Table(
    "accounts", meta, 
    Column("username", String(255)),
    Column("full_name", String(255)),
    Column("profile_pic_url", Text),
    Column("biography", String(255)),
    Column("external_url", String(255)),
    Column("url", String(4000)),
    Column("follows_count", Integer),
    Column("followed_by_count", Integer),
    Column("media_count", Integer),
    Column("is_private", Boolean),
    Column("is_verified", Boolean),
    Column("id", String(255), primary_key=True),
    Column("is_active", Boolean, default=True),
    Column("date_create", DateTime, default=datetime.utcnow()),
)

meta.create_all(engine)