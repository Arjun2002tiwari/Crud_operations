from fastapi import FastAPI
# from models import User
import api
# from sqlalchemy.orm import Session
# from database import Base, SessionLocal
# Initialize the app


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



app = FastAPI()

app.include_router(api.router)

@app.get('/')
def root_api():
    return {"message": "Welcome to CRUD App"}


# @app.get("/user_info/{user_id}")
# def user_info(user_id:int,db: SessionLocal = Depends(get_db)):
#     return db.query(User).get(user_id)


# @app.put("/update_info")
# def update_info(user_id:int,email:str,db: SessionLocal = Depends(get_db)):
#     user=db.query(User).filter(User.id==user_id).first()

#     if user:
#         user.email=email
#         db.commit()
#         db.refresh(user)
#         db.close()
#         return user
#     db.close()
#     return user
    



