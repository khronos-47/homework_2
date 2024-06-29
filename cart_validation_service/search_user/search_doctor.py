from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from cart_validation_service.database.models.user_model import DoctorAccount

from .search_factory import AbstractSearch


class SearchDoctors(AbstractSearch):
    @staticmethod
    async def search(session: AsyncSession, user_id: int) -> tuple[str, int]:
        db_url_query = select(DoctorAccount).where(DoctorAccount.id == user_id)
        db_url = session.scalar(db_url_query)
        if not db_url:
            return None, None
        return "doctor", db_url.specialty_id
