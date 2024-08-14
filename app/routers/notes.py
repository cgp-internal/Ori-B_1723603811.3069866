from fastapi import APIRouter, HTTPException
from app.models import Note
from app.database import db_async_session
from sqlalchemy.future import select
from typing import List

notes_router = APIRouter(prefix="/notes", tags=["notes"])


@notes_router.get("/", response_model=List[Note])
async def read_all_notes():
    async with db_async_session() as session:
        result = await session.execute(select(Note))
        notes = result.scalars().all()
        return notes


@notes_router.post("/", response_model=Note)
async def create_note(note: Note):
    async with db_async_session() as session:
        session.add(note)
        await session.commit()
        return note


@notes_router.get("/{note_id}", response_model=Note)
async def read_note(note_id: int):
    async with db_async_session() as session:
        result = await session.execute(select(Note).where(Note.id == note_id))
        note = result.scalars().first()
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note


@notes_router.put("/{note_id}", response_model=Note)
async def update_note(note_id: int, note: Note):
    async with db_async_session() as session:
        result = await session.execute(select(Note).where(Note.id == note_id))
        db_note = result.scalars().first()
        if db_note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        db_note.title = note.title
        db_note.content = note.content
        await session.commit()
        return db_note


@notes_router.delete("/{note_id}")
async def delete_note(note_id: int):
    async with db_async_session() as session:
        result = await session.execute(select(Note).where(Note.id == note_id))
        note = result.scalars().first()
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"message": "Note deleted successfully"}

notes_router