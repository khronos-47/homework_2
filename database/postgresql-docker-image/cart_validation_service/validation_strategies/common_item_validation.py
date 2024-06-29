from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.base_model import Specialty,CommonItem,SpecialItem,ReceiptItem
from database.models.base_model import UserAccount, DoctorAccount, Receipt
from validation_strategies.validation_factory import Validate

class CommonItemValidation(Validate):
    @staticmethod
    async def validate(session: AsyncSession, user_id: int,user_type: str,  item_id: int )->dict:

        db_url_query = select(CommonItem).where(CommonItem.id == item_id)
        db_url =  session.scalar(db_url_query) 
        if db_url == None:
            return {"item_id": item_id, "problem": "ITEM_NOT_FOUND"}
        if user_type == "NO_USER":
            return {"item_id": item_id, "problem": "NO_USER"}
        return 