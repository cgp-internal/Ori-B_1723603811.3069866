from fastapi import FastAPI
from app.app_config import app_config
from app.routers import notes_router
from app.database import async_session
from app.models import Note
from app.schemas import NoteSchema

app = FastAPI(title="Notes API", version="1.0")

@app.on_event("startup")
async def startup_event():
    await async_session()

@app.on_event("shutdown")
async def shutdown_event():
    await async_session().close()

app.include_router(notes_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=app_config.database_port)