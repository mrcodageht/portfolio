from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from app.data.dao.user_dao import UserDao
from app.models.project_model import UserModel
from app.schemas.user_schema import UserCreation, UserResetPassword, UserChangePassword
from app.services.services_auth import validate_token, get_password_hash
from app.config.env import settings

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")
class UserService:
    def __init__(self, dao: UserDao = Depends(UserDao)):
        self.dao = dao
# Checks if the user token is valid and returns the user
    def require_user(self, token: str = Depends(oauth2_scheme)) -> UserModel:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        print(f"===> Token : {token}")
        token_decoded = validate_token(token)

        user = self.dao.get_user_by_email(token_decoded.sub)
        if user is None:
            raise credentials_exception

        return user

# Creates the default admin user if it doesn't exist
    def create_default_admin(self) -> None:
        existing = self.dao.get_user_by_email(settings.DEFAULT_ADMIN_EMAIL)
        if existing is None:
            hashed = get_password_hash(settings.DEFAULT_ADMIN_PASSWORD)
            self.dao.create_user(
                UserCreation(
                    first_name=settings.DEFAULT_ADMIN_FIRST_NAME,
                    last_name=settings.DEFAULT_ADMIN_LAST_NAME,
                    email=settings.DEFAULT_ADMIN_EMAIL,
                    hashed_password=hashed,
                    admin=True,
                )
            )
            
    def default_admin(self) -> UserModel:
        user = self.dao.get_user_by_email(settings.DEFAULT_ADMIN_EMAIL)
        return user

    def update_password(self, payload_reset: UserResetPassword | None = None, payload_change: UserChangePassword | None = None ) -> bool:
        if payload_reset:
            hashed_password = get_password_hash(payload_reset.new_password)
            user = self.dao.update_password(hashed_password=hashed_password)
            return user.hashed_password == hashed_password
        return False

def get_dao():
    return UserDao()

# Checks if the admin token is valid and that the user is and admin, then return the user
def require_admin(token: str = Depends(oauth2_scheme), service: UserService = Depends(UserService)) -> UserModel:
    user = service.require_user(token)
    token_decoded = validate_token(token)
    if not token_decoded.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return user