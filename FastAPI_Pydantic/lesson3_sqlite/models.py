from sqlalchemy import Column, Integer, String
from lesson3_sqlite.database import Base

# create a Book model
class Books(Base):
    __tablename__ = "books"      # table name from sqlalchemy

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)