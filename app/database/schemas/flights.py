from datetime import datetime
from pydantic import BaseModel

class Flight(BaseModel):
    id : int
    ts_departure : datetime
    ts_arrival :datetime
    destination_city : str
    departure_city : str
    status : str
    available_seats: str

    class Config:
        orm_mode = True