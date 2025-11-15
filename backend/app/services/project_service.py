from ..repos.project_repository import ProjectRepository


class Project:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository
