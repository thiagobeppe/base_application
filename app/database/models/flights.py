from database.session import Base

from sqlalchemy import String,DateTime,Integer,Column


class Flight(Base):
    __tablename__='flights'
    id=Column(Integer,primary_key=True)
    ts_departure=Column(DateTime,nullable=False)
    ts_arrival=Column(DateTime,nullable=False)
    destination_city=Column(String, nullable=False)
    departure_city =Column(String, nullable=False)
    status =Column(String, nullable=False)
    available_seats=Column(Integer, nullable=False)

    def __repr__(self):
        return f"""<flight_number:{self.id}, 
                    ts_departure:{self.ts_departure}, 
                    ts_arrival:{self.ts_arrival}, 
                    destination_city:{self.destination_city}, 
                    departure_city{self.departure_city},
                    status:{self.status},
                    available_seats:{self.available_seats}>"""