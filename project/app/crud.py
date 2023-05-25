from sqlalchemy.orm import Session
from . import models, schemas


def get_data(db: Session):
    return db.query(models.Hindalco).all()


def upload_data(db: Session, data: schemas.HindalcoData):
    db_data = models.Hindalco(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data