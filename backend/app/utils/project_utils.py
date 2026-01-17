import base64
import uuid
import requests
from starlette import status as s

from fastapi import HTTPException

from app.schemas.project_schema import ProjectUpdate, ProjectGithub, ProjectGitlab
from app.schemas.enums import Visibility, Status
def generate_short_id6():
    uid = uuid.uuid4()
    
    uid_bytes = uid.bytes 
    
    b64 = base64.b64encode(uid_bytes).decode('utf-8')
    
    return b64.replace('=', '').replace('/', 'B').replace('+', 'A')[:6] 


def get_external_project(url: str, header: str, provider: str, q: str):
    try:
        response = requests.get(
            url=url,
            headers=header,
            timeout=3
        )
        if response.status_code == s.HTTP_200_OK:
            repo_data = response.json()
            project_update: ProjectUpdate = ProjectUpdate()
            project_update.status = Status.IN_PROGRESS
            project_update.visibility = Visibility.PUBLISHED
            if provider == "gitlab":
                repo = ProjectGitlab(**repo_data)
                if repo.visibility == "private":
                    project_update.visibility=Visibility.PRIVATE,

            else:
                repo = ProjectGithub(**repo_data)
                if repo.private:
                    project_update.visibility=Visibility.PRIVATE,
                project_update.repo_url = repo.svn_url
            
            project_update.title=repo.name
            project_update.description=repo.description
            project_update.start_at=repo.created_at
            return project_update

        elif response.status_code == s.HTTP_404_NOT_FOUND:
            raise HTTPException(detail=f"Repo or project not found with the name '{q}'", status_code=s.HTTP_404_NOT_FOUND)
        raise HTTPException(detail="Error to fetch data", status_code=response.status_code)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error : {e}")
        raise HTTPException(
            detail="Failed to fetch data to github",
            status_code=s.HTTP_500_INTERNAL_SERVER_ERROR
        )

    