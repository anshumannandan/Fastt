from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/data/", response_model=schemas.HindalcoData)
def post_data(data: schemas.HindalcoData, db: Session = Depends(get_db)):
    return crud.upload_data(db=db, data=data)


@app.get("/data/", response_model=list[schemas.HindalcoData])
def get_data(db: Session = Depends(get_db)):
    return crud.get_data(db)