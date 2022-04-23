from datetime import datetime
import deps
from database.models.flights import Flight as flight_model
from database.schemas.flights import Flight, FlightCreate, FlightUpdate

from datetime import datetime
from fastapi import Depends, APIRouter

from typing import List

flights_router = APIRouter()


def _transform_datetime(str_date: str) -> datetime:
    return datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")


@flights_router.get("/flights", status_code=200, response_model=List[Flight])
def get_all_flights(*, db=Depends(deps.get_db)):
    flights = db.query(flight_model).all()
    return flights


@flights_router.get("/flight/{flight_id}", status_code=200, response_model=List[Flight])
def get_single_flight(*, db=Depends(deps.get_db), flight_id: int):
    flight = db.query(flight_model).filter(flight_model.id == flight_id).all()
    return flight


@flights_router.post("/flight", status_code=201, response_model=FlightCreate)
def create_flight(*, db=Depends(deps.get_db), flight_reccord: FlightCreate):

    flight_object = flight_model(
        ts_departure=_transform_datetime(flight_reccord.ts_departure),
        ts_arrival=_transform_datetime(flight_reccord.ts_arrival),
        destination_city=flight_reccord.destination_city,
        departure_city=flight_reccord.departure_city,
        status=flight_reccord.status,
        available_seats=int(flight_reccord.available_seats),
    )

    db.add(flight_object)
    db.commit()
    return flight_reccord


@flights_router.put("/flight/{flight_id}", status_code=200)
def update_flight(
    *, db=Depends(deps.get_db), flight_id: int, flight_value: FlightUpdate
):
    actual_reccord = db.query(flight_model).filter(flight_model.id == flight_id).one()

    actual_reccord.id = (actual_reccord.id,)
    actual_reccord.ts_departure = (
        actual_reccord.ts_departure
        if flight_value.ts_departure is None
        else _transform_datetime(flight_value.ts_departure),
    )
    actual_reccord.ts_arrival = (
        actual_reccord.ts_arrival
        if flight_value.ts_arrival is None
        else _transform_datetime(flight_value.ts_arrival),
    )
    actual_reccord.destination_city = (actual_reccord.destination_city,)
    actual_reccord.departure_city = (actual_reccord.departure_city,)
    actual_reccord.status = (
        actual_reccord.status if flight_value.status is None else flight_value.status,
    )
    actual_reccord.available_seats = (
        actual_reccord.available_seats
        if flight_value.available_seats is None
        else flight_value.available_seats
    )
    db.commit()
    db.refresh(actual_reccord)
    return {"message": f"The reccord with id {flight_id} was deleted with successful"}


@flights_router.delete("/flight/{flight_id}", status_code=200)
def delete_flight(*, db=Depends(deps.get_db), flight_id: int):
    flight = db.query(flight_model).filter(flight_model.id == flight_id).one()
    db.delete(flight)
    db.commit()
    return {"message": f"The reccord with id {flight_id} was deleted with successful"}
