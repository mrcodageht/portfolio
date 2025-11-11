from typing import List

from app.data.simulation.simulation_data import stations
from app.services.model.model_station import Station


def get_all_stations() -> List[Station]:
    return stations # Seulement un placeholder. Aller chercher les données dans la base de données.
