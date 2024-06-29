from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from cart_validation_service.database.models import SpecialItem

from .validation_factory import Validate


class SpecialItemValidation(Validate):
    @staticmethod
    async def validate(session: AsyncSession, user_id: int, user_type: str, type_id: int, item_id: int) -> dict:

        db_url_query = select(SpecialItem).where(SpecialItem.id == item_id)
        db_url = session.scalar(db_url_query)
        if db_url == None:
            return {"item_id": item_id, "problem": "ITEM_NOT_FOUND"}

        if user_type == "NO_USER":
            return {"item_id": item_id, "problem": "NO_USER_SPECIAL_ITEM"}

        if user_type != "doctor":
            return {"item_id": item_id, "problem": "ITEM_IS_SPECIAL"}

        if type_id != db_url.specialty_id:
            return {"item_id": item_id, "problem": "ITEM_SPECIAL_WRONG_SPECIFIC"}

        return
