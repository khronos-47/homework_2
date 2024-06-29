from typing import List

from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from cart_validation_service.database.database import get_db

# from .schemas.query import QueryResponse,QueryRequest
from cart_validation_service.search_user.user_validate import Users
from cart_validation_service.validation_strategies import item_validation


api_router = APIRouter()


@api_router.get("/check", response_class=JSONResponse)
async def make_validate(
    user_id: int,
    item_id: List[str] = Query(...),
    session: AsyncSession = Depends(get_db),
):

    user_type, type_id = await Users.validate(session, user_id)
    results = []
    for sid in item_id:
        sid = sid.lower()
        item_type, item_actual_id = sid.split("_", 1)

        print(item_type, "   ", item_actual_id)
        try:
            item_actual_id = int(item_actual_id)
        except:
            result = {"item_id": sid, "problem": "INCORRECT_ITEM_ID"}
            print(result)
            results.append(result)
            continue
        for item in item_validation.keys():
            if item_type == item:
                result = await item_validation[item].validate(session, user_id, user_type, type_id, item_actual_id)
                print(result, "--- RESULT  ---- ", type(result))
                break
        else:
            result = {"item_id": sid, "problem": "WRONG_CATEGORY"}
        if result is not None:
            print(result)
            result["item_id"] = sid
            results.append(result)
    print("\nRESULTS: ", results, "\n")

    return JSONResponse(results, status_code=200)
