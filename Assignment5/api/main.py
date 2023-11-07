from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas
from .controllers import sandwiches as sandwiches_controller
from .controllers import resources as resources_controller
from .controllers import recipes as recipes_controller
from .controllers import orders as orders_controller
from .controllers import order_details as order_details_controller
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


# Resources Endpoints
@app.get("/resources/", response_model=list[schemas.Resource], tags=["resources"])
def read_all_resources(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return resources_controller.read_all_resources(db=db).offset(skip).limit(limit).all()


# Recipes Endpoints
@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["recipes"])
def read_all_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return recipes_controller.read_all_recipes(db=db).offset(skip).limit(limit).all()


# Orders Endpoints
@app.get("/orders/", response_model=list[schemas.Order], tags=["orders"])
def read_all_orders(skip: int = 0, limit: int = 10):
    return orders_controller.read_all_orders().offset(skip).limit(limit).all()


# Order Details Endpoints
@app.get("/order-details/", response_model=list[schemas.OrderDetail], tags=["order-details"])
def read_all_order_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return order_details_controller.read_all_order_details(db=db).offset(skip).limit(limit).all()
