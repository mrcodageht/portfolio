from pydantic import BaseModel


class Bike(BaseModel):
    code: str

    def __eq__(self, other):
        if not isinstance(other, Bike):
            return NotImplemented
        return self.code == other.code