from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app import landing_page
from app.config.env import settings
from app.routers import project_router
from app.routers import technology_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)


@app.get("/", response_class=HTMLResponse)
def root():
    return landing_page.landing_page


app.include_router(project_router.router, prefix="/api/v1")
app.include_router(technology_router.router, prefix="/api/v1")
