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
