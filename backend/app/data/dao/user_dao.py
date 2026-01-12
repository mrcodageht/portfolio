
from fastapi.params import Depends
from fastapi import HTTPException
from starlette import status
from app.data.database import get_db
from sqlalchemy.orm import Session

from app.models.project_model import UserModel
from app.schemas.user_schema import UserCreation
from app.config.env import settings

class UserDao:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user_by_email(self, email: str) -> UserModel | None:
        user = self.db.query(UserModel).filter(UserModel.email==email).first()
        return user

    def create_user(self, user_create: UserCreation) -> UserModel:
        user = UserModel(**user_create.model_dump(exclude_unset=True))
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except Exception as e:
            print(f"Error : {e}")
            raise ValueError(f"Error : {e}")
        
    def update_password(self, hashed_password: str) -> UserModel:
        user = self.db.query(UserModel).filter_by(email=settings.DEFAULT_ADMIN_EMAIL).one()
        if user is None:
            raise HTTPException(
                detail="config error, user not found",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        try:
            user.hashed_password = hashed_password
            user.is_valid = True
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback()
            print(f"Error : {e}")
            raise HTTPException(
                detail="Error updating user",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
