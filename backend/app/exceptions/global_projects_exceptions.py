from fastapi import HTTPException
from starlette import status
class ProjectException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ProjectNotFoundWithPidException(ProjectException):
    def __init__(self, pid):
        message = f"Project not found with the pid '{pid}'."
        self.message = message
        super().__init__(message)
    
class ProjectAlreadyExistsWithSlugException(ProjectException):
    def __init__(self, slug):
        message = f"A project is already exists with the slug '{slug}'."
        self.message = message
        super().__init__(message=message)

class ProjectNotFoundWithSlugException(ProjectException):
    def __init__(self, slug):
        message = f"Project not found with the slug '{slug}'."
        self.message = message
        super().__init__(message)

def http_404_project_pid(pid):
    return HTTPException(
        detail=f"Project not found with the pid '{pid}'",
        status_code=status.HTTP_404_NOT_FOUND
    )

def http_404_collaborator_id(cid):
    raise HTTPException(
        detail=f"Collaborator not found with the id '{cid}'",
        status_code=status.HTTP_404_NOT_FOUND
    )

def http_404_collaborator_project(cid):
    raise HTTPException(
        detail=f"Collaborator with the id '{cid}' not found in the project",
        status_code=status.HTTP_404_NOT_FOUND
    )