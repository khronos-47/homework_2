from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from validation_strategies.common_item_validation import CommonItemValidation
from validation_strategies.prescription_item_validation import PrescriptionItemValidation
from validation_strategies.special_item_validation import SpecialItemValidation
from database.database import get_db
from starlette import status
from typing import List
from fastapi import Query
from fastapi.responses import JSONResponse

from sqlalchemy import delete, exists, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID
import json
from database.models.base_model import Specialty,CommonItem,SpecialItem,ReceiptItem
from database.models.base_model import UserAccount, DoctorAccount, Receipt
from shema.query import QueryResponse,QueryRequest
from search_user.user_validate import Users
app = FastAPI()

@app.get(
    "/check",
    response_class = JSONResponse
)
async def make_validate(
   user_id:int,
   item_id: List[str] = Query(...),

        session: AsyncSession = Depends(get_db),
):  
    user_type, type_id = await Users.validate(session,user_id)
    results =[]
    #await datadb(session)
    for sid in item_id:
        sid = sid.lower()
        item_type, item_actual_id = sid.split('_', 1)

        print(item_type,"   ",item_actual_id)
        try:
            item_actual_id = int(item_actual_id)
        except:
            result = {"item_id": sid, "problem": "INCORRECT_ITEM_ID" }
            print(result)
            results.append(result)
            continue
        if item_type == 'common':
            result = await CommonItemValidation.validate(session, user_id,user_type, item_actual_id)
        elif item_type == 'receipt':
            result = await PrescriptionItemValidation.validate(session, user_id,user_type, type_id, item_actual_id)
        elif item_type == 'special':
            result = await SpecialItemValidation.validate(session, user_id,user_type, type_id, item_actual_id)
        else:
            result = {'item_id': sid,'problem' :"WRONG_CATEGORY"}
        if result != None:
            print(result)
            result['item_id']= sid
            results.append(result)
    print("\nRESULTS: ",results,"\n")


    return JSONResponse(results,status_code=200) 


async def datadb(session):
    db_url_query = select(UserAccount)
    db_url =  session.query(UserAccount).all()
    print("----------------")
    for i in db_url:
        print(i.id,"  " , i.full_name)
    print("----------------------")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host='0.0.0.0', 
        port=7432, 
        reload = True,
        reload_dirs= 'cart_validation_service',
        log_level="debug",)
