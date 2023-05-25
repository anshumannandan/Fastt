from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base


class Hindalco(Base):

    __tablename__ = "hindalco_data"

    id_        = Column(Integer, primary_key=True)
    datetime_  = Column(DateTime)
    close      = Column(Float)
    high       = Column(Float)
    low        = Column(Float)
    open_      = Column(Float)
    volume     = Column(Integer)
    instrument = Column(String)
