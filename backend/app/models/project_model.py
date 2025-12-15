from typing import List
from sqlalchemy import Column, FetchedValue, String, TIMESTAMP, ForeignKey, func, Enum as SQLEnum, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.data.database import Base
from app.schemas.enums import Kind, Type, Status, Visibility
from app.utils.project_utils import generate_short_id6

technologies_project = Table(
    "technologies_project",
    Base.metadata,
    Column(
        "project_pid", ForeignKey("projects.pid"), primary_key=True, nullable=False
    ),
    Column(
        "technology_id", ForeignKey("technologies.id"), primary_key=True, nullable=False
    )
)

collaborator_project= Table(
    "collaborator_project",
    Base.metadata,
    Column("collaborator_id",ForeignKey("collaborators.id")),
    Column("project_pid", ForeignKey("projects.pid"))
)

class CollaboratorModel(Base):
    __tablename__ = "collaborators"
    id = Column(String(50), primary_key=True, server_default="uuid()")
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    role = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)

    projects = relationship(
        "ProjectModel", secondary="collaborator_project", back_populates="collaborators"
    )


class TechnologyModel(Base):
    __tablename__ = "technologies"
    id : Mapped[str] = mapped_column(primary_key=True, default=generate_short_id6)
    name = Column(String(255), nullable=False)
    slug = Column(String(150), unique=True)
    type = Column(
        SQLEnum(Type, native_enum=False),
        nullable=False
    )
    icon_url = Column(String)

    projects = relationship(
        "ProjectModel", secondary="technologies_project", back_populates="technologies"
    )

class ProjectImageModel(Base):
    __tablename__ = "project_image"
    id : Mapped[str] = mapped_column(primary_key=True)
    image_url = Column(String, nullable=False)
    alt_text = Column(String, nullable=False)
    kind = Column(
        SQLEnum(Kind, native_enum=False), nullable=False, default=Kind.SCREENSHOT
    )

    project_pid : Mapped[str] = mapped_column(ForeignKey("projects.pid"))

# --- Project
class ProjectModel(Base):
    __tablename__ = "projects"

    pid : Mapped[str] =  mapped_column(primary_key=True, default=generate_short_id6)
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
    images: Mapped[List[ProjectImageModel]] = relationship()

    collaborators : Mapped[List[CollaboratorModel]] = relationship(
        secondary=collaborator_project
    )
    technologies : Mapped[List[TechnologyModel]] = relationship(
        secondary=technologies_project
    )








