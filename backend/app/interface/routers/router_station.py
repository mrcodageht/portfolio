from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from app.interface.model_view.view_station import StationView
from app.services.services_station import list_stations

router = APIRouter(prefix="/stations", tags=["stations"])

stations = [
    StationView(
        id=6001,
        name="Drummond / de Maisonneuve",
        longitude=-73.57633531093597,
        latitude=45.4996545106653,
        nb_anchors=27,
        nb_bikes_available=12
    ),
    StationView(
        id=6002,
        name="Ste-Catherine / Dézéry",
        longitude=-73.54099988937377,
        latitude=45.539385081961676,
        nb_anchors=27,
        nb_bikes_available=9
    ),
    StationView(
        id=6003,
        name="Clark / Evans",
        longitude=-73.56784343719482,
        latitude=45.51109876719028,
        nb_anchors=19,
        nb_bikes_available=7
    ),
    StationView(
        id=6004,
        name="du Champ-de-Mars / Gosford",
        longitude=-73.55400860309601,
        latitude=45.50965520472071,
        nb_anchors=23,
        nb_bikes_available=15
    ),
    StationView(
        id=6005,
        name="Brittany / Ainsley",
        longitude=-73.65003436803818,
        latitude=45.52588991809354,
        nb_anchors=23,
        nb_bikes_available=10
    ),
    StationView(
        id=6006,
        name="Ann / Wellington",
        longitude=-73.55676591396332,
        latitude=45.494520387544334,
        nb_anchors=15,
        nb_bikes_available=6
    ),
    StationView(
        id=6007,
        name="Ste-Catherine / de Bullion",
        longitude=-73.56280624866486,
        latitude=45.51113072062821,
        nb_anchors=23,
        nb_bikes_available=8
    ),
    StationView(
        id=6008,
        name="Ste-Catherine / Sanguinet",
        longitude=-73.56124520301817,
        latitude=45.512936177874096,
        nb_anchors=43,
        nb_bikes_available=21
    ),
    StationView(
        id=6009,
        name="Crescent / de Maisonneuve",
        longitude=-73.57759594917297,
        latitude=45.49812041247333,
        nb_anchors=23,
        nb_bikes_available=11
    ),
    StationView(
        id=6901,
        name="Duchesneau / de Grosbois",
        longitude=-73.53121519088745,
        latitude=45.61129437823982,
        nb_anchors=23,
        nb_bikes_available=14
    )
]

@router.get("/", response_model=list[StationView])
def get_stations():
    return list_stations()

@router.get("/{station_id}", response_model=StationView)
def get_station_by_id(station_id: int):
    for station in stations:
        if station.id == station_id:
            return station
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Station inexistante")

@router.post("/", response_model=StationView, status_code=status.HTTP_201_CREATED)
def create_station(station: StationView):
    # Vérifier si l'id ou le nom existent déjà
    if any(s.id == station.id for s in stations):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Une station avec cet identifiant existe déjà.")
    if any(s.name.lower() == station.name.lower() for s in stations):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Une station avec ce nom existe déjà.")

    stations.append(station)
    return station

@router.put("/{station_id}", response_model=StationView)
def replace_station(station_id: int, nouvelle_station: StationView):
    if any(s.name.lower() == nouvelle_station.name.lower() for s in stations):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Une station avec ce nom existe déjà.")

    nouvelle_station.id = station_id

    for index, station in enumerate(stations):
        if station.id == station_id:
            stations[index] = nouvelle_station
            return JSONResponse(content=nouvelle_station.model_dump(), status_code=status.HTTP_200_OK)

    stations.append(station)

    return JSONResponse(content=nouvelle_station.model_dump(), status_code=status.HTTP_201_CREATED)

@router.delete("/{station_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_station_by_id(station_id: int):
    for index, station in enumerate(stations):
        if station.id == station_id:
            stations.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Station inexistante")
