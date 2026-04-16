from database import Base
from sqlalchemy import Column,Integer,String,Text
class  NoteTable(Base):
    __tablename__ = "Notes"
    id = Column(Integer,primary_key=True,)
    title = Column(String)
    content = Column(Text)
    priority = Column(Integer, default=3)
