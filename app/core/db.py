from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import config
from app.core.constants import DATABASE_URL


class PreBase:
    @declared_attr
    def __tablename__(cls):  # noqa
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(DATABASE_URL.format(
    DB_USERNAME=config.DB_USERNAME,
    DB_PASSWORD=config.DB_PASSWORD.get_secret_value(),
    DB_HOST=config.DB_HOST,
    DB_PORT=config.DB_PORT,
    DB_NAME=config.DB_NAME,
))

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
