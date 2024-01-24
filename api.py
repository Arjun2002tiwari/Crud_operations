from fastapi import APIRouter, Depends
from crud import update_user_last_name,get_user_by_id,delete_user_by_id
from sqlalchemy.orm import Session
from database import get_db

router =APIRouter()

@router.get("/user/{user_id}")
def get_user(user_id:int,session:Session=Depends(get_db)):
    try:
        user_info=get_user_by_id(session,user_id)
    finally:
        return user_info
    

@router.put("/user_update/{user_id}")
def update_user(user_id:int,email:str,session: Session = Depends(get_db)):
    try:
        user_info = update_user_last_name(session, user_id,email)
    finally:
       return user_info
    

@router.delete("/user_delete/{user_id}")
def delete_user(user_id:int,session:Session=Depends(get_db)):
        user_info=delete_user_by_id(session,user_id)
        return {user_info}
