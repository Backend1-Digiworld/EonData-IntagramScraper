from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Text
from src.settings.database import meta, engine

InstagramCommentModel = Table(
    "new_comments", meta,  
    Column("POST", String(255)),
    Column("TYPE", String(255)),
    Column("ID", Integer),
    Column("DATE", DateTime),
    Column("TEXT", Text),
    Column("OWNER_ID", Integer),
    Column("OWNER_USERNAME", String(255)),
    Column("OWNER_URL", String(4000)),
    Column("LIKES", Integer),
    Column("date_create", DateTime, default=datetime.utcnow()),
)

meta.create_all(engine)