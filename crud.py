from sqlalchemy.orm import Session
from models import User



def get_user_by_id(db: Session, _id: int):
    return db.query(User).get(_id)


def update_user_last_name(db:Session,user_id:int,email:str):
    user=db.query(User).filter(User.id==user_id).first()

    if user:
        user.email=email
        db.commit()
        db.refresh(user)
        db.close()
        return user
    db.close()
    return user


def delete_user_by_id(db:Session,user_id:int):
    user_info=get_user_by_id(db,user_id)

    if user_info:
        db.delete(user_info)
        db.commit()
        return(user_info)
    return user_info
