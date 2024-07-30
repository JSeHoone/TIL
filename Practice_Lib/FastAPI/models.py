from sqlalchemy import Column, Integer, VARCHAR, DateTime
from datetime import datetime

from database import base


class User(base):
    __tablename__ = "Users"

    user_no = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(VARCHAR(10), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    hashed_pw = Column(VARCHAR(100), nullable=False)
    role = Column(VARCHAR(20), nullable=False, default="MEMBER")
    status = Column(VARCHAR(1), nullable=False, default="1")
    regdate = Column(DateTime, nullable=False, default=datetime.now)