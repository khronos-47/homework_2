from enum import Enum
from typing import List, Optional

from fastapi.exceptions import HTTPException
from pydantic import UUID4, BaseModel, Field, HttpUrl, root_validator, validator
from starlette import status


class QueryResponse(BaseModel):
    asnwer: List[str] = Field(..., alias="item_id")


class QueryRequest(BaseModel):
    user_id: int
    item_id: List[str] = Field(..., alias="item_id")
