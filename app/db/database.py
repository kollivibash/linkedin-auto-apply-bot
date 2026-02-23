from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.db.models import Base

DATABASE_URL = "sqlite+aiosqlite:///./jobs.db"

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
