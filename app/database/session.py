import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
