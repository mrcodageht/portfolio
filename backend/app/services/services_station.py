from typing import List

from app.data.data_station import get_all_stations
from app.interface.model_view.view_station import StationView
from app.services.model.model_station import Station


def convert_stations_to_view(station: Station) -> StationView:
    return StationView(
        id=station.id,
        name=station.name,
        longitude=station.longitude,
        latitude=station.latitude,
        nb_anchors=station.nb_anchors,
        nb_bikes_available=len(station.bikes)
    )

def list_stations() -> List[StationView]:
    stations = get_all_stations()
    return [convert_stations_to_view(s) for s in stations]
