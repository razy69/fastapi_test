from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from app import SETTINGS

Base: DeclarativeMeta = declarative_base()

engine = create_engine(
    SETTINGS.database_uri,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
