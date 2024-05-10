from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import config

DATABASE_URL = "postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    DB_USERNAME=config.DB_USERNAME,
    DB_PASSWORD=config.DB_PASSWORD.get_secret_value(),
    DB_HOST=config.DB_HOST,
    DB_PORT=config.DB_PORT,
    DB_NAME=config.DB_NAME,
)


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable, Base):
    pass


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
