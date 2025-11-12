from app.services.model.model_station_base import StationBase


class StationView(StationBase):
    nb_bikes_available: int = 0

    def __eq__(self, other):
        if not isinstance(other, StationView):
            return NotImplemented
        return super().__eq__(other) and self.nb_bikes_available == other.nb_bikes_available