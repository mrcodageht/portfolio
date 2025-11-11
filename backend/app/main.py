from fastapi import FastAPI

from app.config.env import settings
from app.interface.routers import router_station

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)


@app.get("/")
def root():
    return {"message": "Bonjour, API!"}


app.include_router(router_station.router)
