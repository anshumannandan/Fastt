from pydantic import BaseModel
from datetime import datetime


class HindalcoData(BaseModel):

    datetime   : datetime
    close      : float
    high       : float
    low        : float
    open       : float
    volume     : int
    instrument : str

    class Config:
        orm_mode = True