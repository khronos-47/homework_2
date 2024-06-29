from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from cart_validation_service.database.models.user_model import UserAccount

from .search_factory import AbstractSearch


class SerchOrdinaryUser(AbstractSearch):
    @staticmethod
    async def search(session: AsyncSession, user_id: int) -> tuple[str, int]:

        db_url_query = select(UserAccount).where(UserAccount.id == user_id)
        db_url = session.scalar(db_url_query)
        print("--------------------", db_url)
        if not db_url:
            return None, None
        return "User", None
