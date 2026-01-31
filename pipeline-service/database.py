from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time

DATABASE_URL = os.getenv("DATABASE_URL")

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except Exception:
        print("Database not ready, waiting...")
        time.sleep(3)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
