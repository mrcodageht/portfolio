from fastapi import FastAPI

from app.config.env import settings
from app.routers import project_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)


@app.get("/")
def root():
    return {"message": "Bonjour, API!"}


app.include_router(project_router.router)
