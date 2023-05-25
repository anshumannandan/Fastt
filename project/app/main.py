from fastapi import Depends, FastAPI, UploadFile
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine
import csv, codecs
from pydantic import parse_obj_as
from typing import List


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/data/")
def post_data(file: UploadFile, db: Session = Depends(get_db)):
    csv_data = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data_list = parse_obj_as(List[schemas.HindalcoData], list(csv_data))
    db.add_all(models.Hindalco(**data.dict()) for data in data_list)
    db.commit()
    return {'success' : True, 
            'message' : 'Data Uploaded Sucessfully',
            'data' : data_list}


@app.get("/data/", response_model=list[schemas.HindalcoData])
def get_data(db: Session = Depends(get_db)):
    return db.query(models.Hindalco).all()