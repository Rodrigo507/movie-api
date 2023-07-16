from config.database import Base
from sqlalchemy import Column, Integer, String


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    overview = Column(String(50), nullable=False)
