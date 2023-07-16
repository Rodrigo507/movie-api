from sqlalchemy import Column, Integer, String
from config.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(10), nullable=False)
    password = Column(String(10), nullable=False)
    email = Column(String(10), nullable=False)
