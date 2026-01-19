import base64
import uuid
import requests
from starlette import status as s

from fastapi import HTTPException

from app.schemas.project_schema import ProjectUpdate, ProjectGithub, ProjectGitlab
from app.schemas.enums import Visibility, Status
from app.config.env import settings
from app.schemas.user_schema import UserGitlab
def generate_short_id6():
    uid = uuid.uuid4()
    
    uid_bytes = uid.bytes 
    
    b64 = base64.b64encode(uid_bytes).decode('utf-8')
    
    return b64.replace('=', '').replace('/', 'B').replace('+', 'A')[:6] 


def get_external_project(url: str, header: str, provider: str, q: str):
    response = None
    try:
        response = requests.get(
            url=url,
            headers=header,
            timeout=3
        )
    except Exception as e:
        print("Error to fetch data", e)
        raise HTTPException(detail="ERROR to fetch data to provider", status_code=s.HTTP_500_INTERNAL_SERVER_ERROR)

    if response.status_code == s.HTTP_200_OK:
        repo_data = response.json()
        project_update: ProjectUpdate = ProjectUpdate()
        project_update.status = Status.IN_PROGRESS
        project_update.visibility = Visibility.PUBLISHED
        if provider == "gitlab":
            if len(repo_data) == 0:
                raise HTTPException(detail=f"Project not found with the name '{q}'", status_code=s.HTTP_404_NOT_FOUND)
            repo = ProjectGitlab(**repo_data[0])
            if repo.visibility == "private":
               project_update.visibility=Visibility.PRIVATE
            project_update.repo_url = repo.web_url
        else:
            repo = ProjectGithub(**repo_data)
            if repo.private:
                project_update.visibility=Visibility.PRIVATE
            project_update.repo_url = repo.svn_url
        
        project_update.title=repo.name
        project_update.description=repo.description
        project_update.start_at=repo.created_at
        return project_update

    elif response.status_code == s.HTTP_404_NOT_FOUND:
        raise HTTPException(detail=f"Repo or project not found with the name '{q}'", status_code=s.HTTP_404_NOT_FOUND)
    raise HTTPException(detail="Error to fetch data", status_code=response.status_code)
    
def fetch_gitlab_user(url, header):
    response = requests.get(
        url=url,
        headers=header,
        timeout=3
    )

    if response.status_code == s.HTTP_200_OK:
        data = response.json()
        return UserGitlab(**data)
    else:
        print("Error", response)
        raise HTTPException(f"Error to fetch data to gitlab : status code {response.status_code}", s.HTTP_500_INTERNAL_SERVER_ERROR)
    
# end def
    