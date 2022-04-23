from database.session import Base

from sqlalchemy import String, DateTime, Integer, Column


class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    ts_departure = Column(DateTime, nullable=False)
    ts_arrival = Column(DateTime, nullable=False)
    destination_city = Column(String, nullable=False)
    departure_city = Column(String, nullable=False)
    status = Column(String, nullable=False)
    available_seats = Column(Integer, nullable=False)
