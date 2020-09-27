from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Files(Base):
    __tablename__ = 'Files'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255))
    sender_id = Column(String(255))