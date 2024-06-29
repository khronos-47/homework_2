from starlette import status
from enum import Enum
from typing import Optional,List
from fastapi.exceptions import HTTPException
from pydantic import UUID4, BaseModel, Field, HttpUrl, root_validator, validator


class QueryResponse(BaseModel):
	asnwer : List[str] = Field(...,alias= "item_id")

class QueryRequest(BaseModel):
	user_id : int
	item_id: List[str] = Field(...,alias= "item_id")
