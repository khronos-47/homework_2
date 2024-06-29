from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from . import search_user


class Users:
    @staticmethod
    async def validate(session: AsyncSession, user_id: int) -> tuple[str, int]:
        for user in search_user:
            user_type, type_id = await user.search(session, user_id)
            if user_type != None:
                return user_type, type_id

        if user_type == None:
            user_type = "NO_USER"
        print({"user_type": user_type, "type_id": type_id})

        return user_type, type_id
