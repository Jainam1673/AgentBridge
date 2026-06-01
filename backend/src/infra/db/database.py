from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.domain.models.models import Base
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/agentbridge"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    class Config:
        env_file = ".env"

settings = Settings()

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
