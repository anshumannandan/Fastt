from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base


class Hindalco(Base):

    __tablename__ = "hindalco_data"

    id         = Column(Integer, primary_key=True)
    datetime   = Column(DateTime)
    close      = Column(Float)
    high       = Column(Float)
    low        = Column(Float)
    open       = Column(Float)
    volume     = Column(Integer)
    instrument = Column(String)