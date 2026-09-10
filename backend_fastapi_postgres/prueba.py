from sqlmodel import SQLModel, create_engine, Session
from src.app.core.config import settings

engine = create_engine(
    "postgresql://user:password@localhost/dbname",
    echo=False,
    pool_pre_ping=True,
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)