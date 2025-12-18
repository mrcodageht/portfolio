from datetime import datetime

from fastapi.params import Depends


from app.data.database import get_db
from sqlalchemy.orm import Session

from app.models.project_model import UserModel
from app.schemas.user_schema import UserCreation

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
