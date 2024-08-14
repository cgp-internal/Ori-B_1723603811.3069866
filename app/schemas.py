from pydantic import BaseModel
from app.models import Note

class NoteBase(BaseModel):
    title: str
    content: str

class NoteSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

NoteCreate = NoteBase
NoteUpdate = NoteBase

__all__ = ["NoteSchema", "NoteBase", "NoteCreate", "NoteUpdate"]