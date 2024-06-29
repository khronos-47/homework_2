from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from cart_validation_service.database.models import ReceiptItem

from .validation_factory import Validate


class PrescriptionItemValidation(Validate):
    @staticmethod
    async def validate(session: AsyncSession, user_id: int, user_type: str, type_id: int, item_id) -> dict:

        db_url_query = select(ReceiptItem).where(ReceiptItem.id == item_id)
        db_url = session.scalar(db_url_query)
        if db_url == None:
            return {"item_id": item_id, "problem": "ITEM_NOT_FOUND"}

        if user_type == "NO_USER":
            return {"item_id": item_id, "problem": "NO_USER_NO_RECEIPT"}

        if (type_id != item_id or user_type == "User") and user_type != "doctor":
            return {"item_id": item_id, "problem": "NO_RECEIPT"}
        return
