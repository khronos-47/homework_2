from sqlalchemy.orm import Session
from database.models.base_model import Specialty,CommonItem,SpecialItem,ReceiptItem
from database.models.base_model import UserAccount, DoctorAccount, Receipt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from search_user.search_factory import Search

class Ordinary_user(Search):
    @staticmethod
    async def search(session: AsyncSession,user_id: int) -> tuple[str, int]:
        
        db_url_query = select(UserAccount).where(UserAccount.id == user_id)
        db_url =  session.scalar(db_url_query)
        print("--------------------",db_url)
        if not db_url:
            return None, None
        return "User" , None