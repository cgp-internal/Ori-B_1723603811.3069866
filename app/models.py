from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.app_config import app_config

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    def __repr__(self):
        return f"Note(id={self.id}, title={self.title}, content={self.content})"

Note  # exposes Note