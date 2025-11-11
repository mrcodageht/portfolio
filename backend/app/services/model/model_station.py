from typing import List

from app.services.model.model_bike import Bike
from app.services.model.model_station_base import StationBase


class Station(StationBase):
    bikes: List[Bike]

    def __eq__(self, other):
        if not isinstance(other, Station):
            return NotImplemented

        return super().__eq__(other) and self.bikes == other.bikes
