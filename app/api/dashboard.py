from fastapi import FastAPI
from sqlalchemy import select
from app.db.database import SessionLocal
from app.db.models import JobApplication

app = FastAPI()

@app.get("/applications")
async def get_applications():
    async with SessionLocal() as session:
        result = await session.execute(select(JobApplication))
        return result.scalars().all()
