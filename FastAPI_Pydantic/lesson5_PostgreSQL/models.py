from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from lesson5_PostgreSQL.database import Base


# create tables to be saved in the PostgreSQL database using SQLAlchemy ORM
class Questions(Base):
    __tablename__ = "questions"      # table name 

    id = Column(Integer, primary_key=True, index=True)     # index improves search performance 
    question_text = Column(String, index=True)


class Choices(Base):
    __tablename__ = "choices"      # table name 
    
    id = Column(Integer, primary_key=True, index=True)  
    choices = Column(String)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
