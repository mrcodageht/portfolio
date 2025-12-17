
from app.schemas.enums import Kind


class ProjectImage:
    id: str
    image_url: str
    alt_text: str
    kind: Kind
