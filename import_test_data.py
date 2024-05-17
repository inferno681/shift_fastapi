import asyncio
import json
from datetime import datetime

from sqlalchemy.dialects.postgresql import insert

from app.core import get_async_session
from app.models import User


async def import_test_data():
    """Функция импорта тестовых данных"""
    with open("test_data.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    for user in users:
        user["created"] = datetime.fromisoformat(user["created"])
        user["next_promotion"] = datetime.fromisoformat(user["next_promotion"])
    async for session in get_async_session():
        await session.execute(
            insert(User).values(users).on_conflict_do_nothing()
        )
        await session.commit()


if __name__ == "__main__":
    asyncio.run(import_test_data())
