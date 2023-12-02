from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import models
from .. import schemas

def create_sandwich(db: Session, sandwich: schemas.SandwichCreate):
    # Create a new instance of the Sandwich model with the provided data
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )
    # Add the newly created Sandwich object to the database session
    db.add(db_sandwich)
    # Commit the changes to the database
    db.commit()
    # Refresh the Sandwich object to ensure it reflects the current state in the database
    db.refresh(db_sandwich)
    # Return the newly created Sandwich object
    return db_sandwich

def read_all_sandwiches(db: Session):
    return db.query(models.Sandwich).all()

def read_one_sandwich(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update_sandwich(db: Session, sandwich_id, sandwich):
    # Query the database for the specific sandwich to update
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    # Extract the update data from the provided 'sandwich' object
    update_data = sandwich.dict(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_sandwich.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated sandwich record
    return db_sandwich.first()

def delete_sandwich(db: Session, sandwich_id):
    # Query the database for the specific sandwich to delete
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    # Delete the database record without synchronizing the session
    db_sandwich.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# CRUD operations for Resources
def create_resource(db: Session, resource: schemas.ResourceCreate):
    # Create a new instance of the Resource model with the provided data
    db_resource = models.Resource(
        item=resource.item,
        amount=resource.amount
    )
    # Add the newly created Resource object to the database session
    db.add(db_resource)
    # Commit the changes to the database
    db.commit()
    # Refresh the Resource object to ensure it reflects the current state in the database
    db.refresh(db_resource)
    # Return the newly created Resource object
    return db_resource

# Implement read_all, read_one, update, and delete operations for resources

# CRUD operations for Recipes
def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    # Create a new instance of the Recipe model with the provided data
    db_recipe = models.Recipe(
        amount=recipe.amount,
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id
    )
    # Add the newly created Recipe object to the database session
    db.add(db_recipe)
    # Commit the changes to the database
    db.commit()
    # Refresh the Recipe object to ensure it reflects the current state in the database
    db.refresh(db_recipe)
    # Return the newly created Recipe object
    return db_recipe

# Implement read_all, read_one, update, and delete operations for recipes

# CRUD operations for Order Details
def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    # Create a new instance of the OrderDetail model with the provided data
    db_order_detail = models.OrderDetail(
        amount=order_detail.amount,
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id
    )
    # Add the newly created OrderDetail object to the database session
    db.add(db_order_detail)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_order_detail)
    # Return the newly created OrderDetail object
    return db_order_detail

# Implement read_all, read_one, update, and delete operations for order_details
