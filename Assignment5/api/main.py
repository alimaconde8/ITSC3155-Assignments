from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas
from .controllers import sandwiches as sandwiches_controller
from .dependencies import database

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Sandwiches Endpoints
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches_controller.create_sandwich(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["sandwiches"])
def read_all_sandwiches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return sandwiches_controller.read_all_sandwiches(db=db).offset(skip).limit(limit).all()


@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = sandwiches_controller.read_one_sandwich(db=db, sandwich_id=sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich


@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    db_sandwich = sandwiches_controller.read_one_sandwich(db=db, sandwich_id=sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches_controller.update_sandwich(db=db, sandwich_id=sandwich_id, sandwich=sandwich)


@app.delete("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = sandwiches_controller.read_one_sandwich(db=db, sandwich_id=sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches_controller.delete_sandwich(db=db, sandwich_id=sandwich_id)
