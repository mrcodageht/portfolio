import uuid
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from starlette import status
from app import landing_page
from app.config.env import settings
from app.data.database import get_db
from app.routers import collaborator_router, project_router, user_router
from app.routers import technology_router
from app.services.services_user import UserService

generated_key = settings.KEY_INIT
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)


@app.get("/", response_class=HTMLResponse)
def root():
    return landing_page.landing_page

@app.post("/init", status_code=status.HTTP_204_NO_CONTENT)
def init(key: str, service: UserService = Depends(UserService)):
    if key == generated_key:
        service.create_default_admin()
    else:
        raise HTTPException(
            detail=f"Not authorized.",
            status_code= status.HTTP_403_FORBIDDEN
        )


app.include_router(project_router.router, prefix="/api/v1")
app.include_router(technology_router.router, prefix="/api/v1")
app.include_router(collaborator_router.router, prefix="/api/v1")
app.include_router(user_router.router, prefix="/api/v1")


def get_service():
    return UserService()