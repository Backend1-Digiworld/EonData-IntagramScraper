from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Text
from ..settings.database import meta, engine

InstagramAcountModel = Table(
    "sessions", meta,  
    Column("username", String(255)),
    Column("password", String(255)),
    Column("last_use", DateTime, default=datetime.utcnow),
    Column("available", Boolean, default=True),
    Column("email", String(255)),
    Column("phone", Integer),
    Column("is_used",  Boolean, default=False),
    Column("is_dead", Boolean, default=False),
    Column("id", Integer, primary_key=True)
)

meta.create_all(engine)