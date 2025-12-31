
from app.data.dao.project_media_dao import ProjectMediaDao
from fastapi import Depends
from app.utils.mapping_utils import map_to_project_media_public
from app.schemas.project_media_schema import *
from app.schemas.enums import Kind
from fastapi import UploadFile, File
from app.config.env import settings

import shutil
from pathlib import Path


class ProjectMediaService:
    def __init__(self, project_media_dao: ProjectMediaDao = Depends(ProjectMediaDao)) -> None:
        self.pmd = project_media_dao

    def get_all_by_pid(self, pid: str, kind: Kind | None = None) -> list[ProjectMediaPublic]:
        medias = self.pmd.find_all_by_project_id(pid=pid, kind=kind)
        return [map_to_project_media_public(m) for m in medias]

    def save(self, pid: str, media_create: ProjectMedia, file: UploadFile = File(...) ):


        media_to_create = ProjectMediaPublic(
            id="",
            alt_text=media_create.alt_text,
            kind=media_create.kind,
            media_url=""
        )
        media_created = self.pmd.create(media_to_create, pid)
        UPLOAD_DIR = Path("medias")
        ext = Path(file.filename).suffix

        filename = f"{str(media_created.id)}{ext}"
        file_path = UPLOAD_DIR / filename
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        media_to_create.media_url =f"{settings.SERVER_MEDIA}/{UPLOAD_DIR}/{filename}"
        print(f"{media_created.media_url} - {media_created.id}")
        print(f"url {media_to_create.media_url} ")
        return map_to_project_media_public(self.pmd.update(media_created.id, media_to_create))
    
    def delete(self, id: str):
        self.pmd.delete(id=id)