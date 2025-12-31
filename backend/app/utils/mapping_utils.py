"""
    All mappings function
"""
from app.models.project_model import CollaboratorModel, ProjectModel, TechnologyModel, ProjectMediaModel
from app.schemas.collaborator_schema import CollaboratorPublic
from app.schemas.project_schema import ProjectPublic, ProjectPublicWithCollaborators, ProjectPublicWithCollaboratorsAndTechnologies, ProjectPublicWithTechnologies
from app.schemas.technology_schema import TechnologyPublic
from app.schemas.project_media_schema import ProjectMediaPublic

def map_to_project(project_model: type[ProjectModel]) -> ProjectPublic:
    return ProjectPublic(
        title=project_model.title,
        pid=str(project_model.pid),
        slug=project_model.slug,
        description=project_model.description,
        start_at=project_model.start_at,
        end_at=project_model.end_at,
        status=project_model.status,
        visibility=project_model.visibility,
        cover_image_url=project_model.cover_image_url,
        live_url=project_model.live_url,
        repo_url=project_model.repo_url,
    )


def map_to_technology_pub(tech_model: TechnologyModel) -> TechnologyPublic:
    techno_pub = TechnologyPublic( 
        name=tech_model.name,
        type=tech_model.type,
        icon_url=tech_model.icon_url,
        slug=tech_model.slug,
        id=tech_model.id
    )
    return techno_pub


def map_to_collaborator_public(collab: CollaboratorModel)-> CollaboratorPublic:
    return CollaboratorPublic(
        first_name=collab.first_name,
        last_name=collab.last_name,
        id=collab.id,
        role=collab.role,
        portfolio_url=collab.portfolio_url,
        github_url=collab.github_url,
        linkedin_url=collab.linkedin_url
    )

def map_to_project_with_technologies(project_model: ProjectModel, techs: list[TechnologyModel])-> ProjectPublicWithTechnologies:
    
    techs_mapped = [map_to_technology_pub(t) for t in techs]
    ppwt = ProjectPublicWithTechnologies(
        title=project_model.title,
        pid=str(project_model.pid),
        slug=project_model.slug,
        description=project_model.description,
        start_at=project_model.start_at,
        end_at=project_model.end_at,
        status=project_model.status,
        visibility=project_model.visibility,
        cover_image_url=project_model.cover_image_url,
        live_url=project_model.live_url,
        repo_url=project_model.repo_url,
        technologies=techs_mapped,
    )
    return ppwt


def map_to_project_with_collaborators(
        project_model: ProjectModel, 
        collabs: list[CollaboratorModel]) -> ProjectPublicWithCollaborators:
    collabs_mapped = [map_to_collaborator_public(c) for c in collabs]
    ppwc = ProjectPublicWithCollaborators(
        title=project_model.title,
        pid=str(project_model.pid),
        slug=project_model.slug,
        description=project_model.description,
        start_at=project_model.start_at,
        end_at=project_model.end_at,
        status=project_model.status,
        visibility=project_model.visibility,
        cover_image_url=project_model.cover_image_url,
        live_url=project_model.live_url,
        repo_url=project_model.repo_url,
        collaborators=collabs_mapped
    )
    return ppwc

def map_to_project_with_technologies_and_collaborators(
        project_model: ProjectModel,
        collabs: list[CollaboratorModel],
        techs: list[TechnologyModel]
) -> ProjectPublicWithCollaboratorsAndTechnologies:
    
    collabs_mapped = [map_to_collaborator_public(c) for c in collabs]
    techs_mapped = [map_to_technology_pub(t) for t in techs]
    ppwcat = ProjectPublicWithCollaboratorsAndTechnologies(
        title=str(project_model.title),
        pid=str(project_model.pid),
        slug=str(project_model.slug),
        description=str(project_model.description),
        start_at=project_model.start_at,
        end_at=project_model.end_at,
        status=project_model.status,
        visibility=project_model.visibility,
        cover_image_url=project_model.cover_image_url,
        live_url=project_model.live_url,
        repo_url=project_model.repo_url,
        collaborators=collabs_mapped,
        technologies=techs_mapped
    )
    return ppwcat

def map_to_project_media_public(project_media: ProjectMediaModel):
    return ProjectMediaPublic(
        alt_text=str(project_media.alt_text),
        kind=project_media.kind,
        id=str(project_media.id),
        media_url=str(project_media.media_url)
    )