from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{"message": "FastAPI + PostgreSQL"}

@app.post("/users", response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    new_user =  models.User(
        name=user.name,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users", response_model=list[schemas.UserResponse])
def list_users(
    db: Session = Depends(get_db)
):
    users = db.query(models.User).order_by(models.User.id).all()
    return users

# Get user by ID:

@app.get(
    "/users/{user_id}",
    response_model=schemas.UserResponse
)


def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user =  db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found" 
        )
    
    return user

# Delete user endpoint:

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if user is None:
        return{
            "error": "User not found"
        }
    
    db.delete(user)
    db.commit()

    return{
        "message": "User deleted successfully!"
    }

# Update user:

@app.put(
    "/users/{user_id}",
    response_model=schemas.UserResponse
)

def update_user(
    user_id: int,
    updated_user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    
    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    user.name = updated_user.name
    user.age = updated_user.age

    db.commit()

    db.refresh(user)

    return user
    

