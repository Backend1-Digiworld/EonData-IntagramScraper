from sqlmodel import create_engine
from settings.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
