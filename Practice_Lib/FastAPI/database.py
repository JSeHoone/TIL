from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///./fastapi.db"

# sqlite는 기본적으로 한번에 하나의 스레드만 DB에 접근할 수 있도록 재한되어 있음.
# create DB Connection Pool
engine = create_engine(DB_URL, pool_size=10, connect_args={"check_same_thread" : False})

# To DB Connection
session_local = sessionmaker(autoflush=False, autocommit = False, bind=engine)

# To use DB model
base = declarative_base()


def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()