from cmath import isclose

from pydantic import BaseModel


class StationBase(BaseModel):
    id: int
    name: str
    longitude: float
    latitude: float
    nb_anchors: int

    def __eq__(self, other):
        if not isinstance(other, StationBase):
            return NotImplemented

        return (
                self.id == other.id
                and self.name == other.name
                and isclose(self.longitude, other.longitude, rel_tol=1e-6, abs_tol=1e-6)
                and isclose(self.latitude, other.latitude, rel_tol=1e-6, abs_tol=1e-6)
                and self.nb_anchors == other.nb_anchors
        )