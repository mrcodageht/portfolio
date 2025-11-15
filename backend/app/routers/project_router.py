from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("")
def get_projects():
    return []

@router.get("/{pid}")
def get_by_id(pid: str):
    return None

@router.post("")
def create():
    return None

@router.put("")
def update():
    return None

@router.delete("")
def delete():
    return None