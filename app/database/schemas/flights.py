from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Flight(BaseModel):
    id : int
    ts_departure : datetime
    ts_arrival :datetime
    destination_city : str
    departure_city : str
    status : str
    available_seats: int

    class Config:
        orm_mode = True

class FlightCreate(Flight):
    id: Optional[int] = None
    ts_departure : str
    ts_arrival :str
    destination_city : str
    departure_city : str
    status : str
    available_seats: int


class FlightUpdate(Flight):
    id: Optional[int] = None
    ts_departure : Optional[str] = None
    ts_arrival : Optional[str] = None
    destination_city : Optional[str] = None
    departure_city : Optional[str] = None
    status : Optional[str] = None
    available_seats: Optional[int] = None