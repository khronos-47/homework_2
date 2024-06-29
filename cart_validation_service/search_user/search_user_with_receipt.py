from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from cart_validation_service.database.models.receipt_model import Receipt

from .search_factory import AbstractSearch


class SearchUserReceipt(AbstractSearch):
    @staticmethod
    async def search(session: AsyncSession, user_id: int) -> tuple[str, int]:

        db_url_query = select(Receipt).where(Receipt.user_id == user_id)
        db_url = session.scalar(db_url_query)
        if not db_url:
            return None, None
        return "receipt", db_url.item_id
