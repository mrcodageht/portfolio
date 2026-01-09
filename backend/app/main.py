from app.schemas.token_schema import KeyInit
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from starlette import status
from app import landing_page
from app.config.env import settings
from app.data.database import get_db
from app.routers import collaborator_router, project_router, user_router
from app.routers import technology_router
from app.schemas.stats_schema import Stats
from app.services.ressource import RessourceService
from app.services.services_user import UserService

from starlette.middleware.cors import CORSMiddleware

generated_key = settings.KEY_INIT
app = FastAPI(title=settings.PROJECT_NAME, version=settings.API_VERSION)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#


@app.get("/", response_class=HTMLResponse)
def root():
    return landing_page.landing_page


@app.post("/api/v1/init", status_code=status.HTTP_204_NO_CONTENT)
def init(payload: KeyInit, service: UserService = Depends(UserService)):
    if payload.key == generated_key:
        service.create_default_admin()
    else:
        raise HTTPException(
            detail=f"Not authorized.", status_code=status.HTTP_403_FORBIDDEN
        )


@app.get("/api/v1/stats", response_model=Stats, status_code=status.HTTP_200_OK)
def stats(services: RessourceService = Depends(RessourceService)):
    return services.get_stats()


app.include_router(project_router.router, prefix="/api/v1")
app.include_router(technology_router.router, prefix="/api/v1")
app.include_router(collaborator_router.router, prefix="/api/v1")
app.include_router(user_router.router, prefix="/api/v1")


def get_service():
    return UserService()


def get_ressource():
    return RessourceService()

