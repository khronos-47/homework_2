from sqlalchemy.orm import Session
from database.models.base_model import Specialty,CommonItem,SpecialItem,ReceiptItem
from database.models.base_model import UserAccount, DoctorAccount, Receipt
from sqlalchemy import select
from search_user.search_doctor import Doctors
from search_user.search_user_with_receipt import UserReceiptId as Receipt
from search_user.search_ordinary_user import Ordinary_user as Ordinary
from sqlalchemy.ext.asyncio import AsyncSession
class Users:
    @staticmethod
    async def validate(session: AsyncSession, user_id: int) ->tuple[str,int]:
        
        user_type , type_id = await Doctors.search(session,user_id)


        if  (user_type == None):
            user_type , type_id = await Receipt.search(session,user_id)  


        if (user_type == None):
            user_type , type_id = await Ordinary.search(session,user_id)  
        print({ "user_type": user_type, "type_id": type_id})

        if user_type == None:
            user_type = "NO_USER"
        print({ "user_type": user_type, "type_id": type_id})

        return user_type,  type_id