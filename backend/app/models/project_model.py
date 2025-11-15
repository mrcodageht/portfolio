from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, func, Enum as SQLEnum
from sqlalchemy.orm import relationship
from data.database import Base
from app.schemas.project_image_schema import Kind
from app.schemas.project_schema import Status, Visibility


# --- Project
class Project(Base):
    __tablename__ = "projects"

    pid = Column(String(50), primary_key=True, index=True, server_default="uuid()")
    title = Column(String(255), nullable=False)
    slug = Column(String(150), unique=True, index=True)
    description = Column(String(1000))  # augmenter la taille
    start_at = Column(TIMESTAMP, server_default=func.now())
    end_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    status = Column(
        SQLEnum(Status, native_enum=False), nullable=False, default=Status.IN_PROGRESS
    )
    visibility = Column(
        SQLEnum(Visibility, native_enum=False),
        nullable=False,
        default=Visibility.PRIVATE,
    )
    cover_image_url = Column(String)  # corrigé
    liveUrl = Column(String)
    repoUrl = Column(String)

    # relations
    project_images = relationship(
        "ProjectImage", back_populates="project", cascade="all, delete-orphan"
    )
    collaborators = relationship(
        "Collaborator",
        secondary="collaborator_project",
        back_populates="projects",
    )
    technologies = relationship(
        "Technology",
        secondary="technologies_project",
        back_populates="projects",
    )


class Technology(Base):
    __tablename__ = "technologies"
    id = Column(String(50), primary_key=True, server_default="uuid()")
    name = Column(String(255), nullable=False)
    slug = Column(String(150), unique=True)
    type = Column(String(150))
    icon_url = Column(String)

    projects = relationship(
        "Project", secondary="technologies_project", back_populates="technologies"
    )


class Collaborator(Base):
    __tablename__ = "collaborators"
    id = Column(String(50), primary_key=True, server_default="uuid()")
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    role = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)

    projects = relationship(
        "Project", secondary="collaborator_project", back_populates="collaborators"
    )


class ProjectImage(Base):
    __tablename__ = "project_image"
    id = Column(String(50), primary_key=True, server_default="uuid()")
    image_url = Column(String, nullable=False)
    alt_text = Column(String, nullable=False)
    kind = Column(
        SQLEnum(Kind, native_enum=False), nullable=False, default=Kind.SCREENSHOT
    )

    project_pid = Column(String(50), ForeignKey("projects.pid"), nullable=False)
    project = relationship("Project", back_populates="project_images")


class CollaboratorProject(Base):
    __tablename__ = "collaborator_project"
    project_pid = Column(
        String(50), ForeignKey("projects.pid"), primary_key=True, nullable=False
    )
    collaborator_id = Column(
        String(50), ForeignKey("collaborators.id"), primary_key=True, nullable=False
    )


class TechnologiesProject(Base):
    __tablename__ = "technologies_project"
    project_pid = Column(
        String(50), ForeignKey("projects.pid"), primary_key=True, nullable=False
    )
    technology_id = Column(
        String(50), ForeignKey("technologies.id"), primary_key=True, nullable=False
    )
