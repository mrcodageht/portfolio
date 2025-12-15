from fastapi import HTTPException


def ex404_techno(identifier: str):
    return HTTPException(
    detail="Technologi"
)