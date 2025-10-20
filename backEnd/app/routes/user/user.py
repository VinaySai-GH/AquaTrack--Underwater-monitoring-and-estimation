from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from sqlalchemy.orm import Session
from app.models.models import User
from app.database.dependency import get_current_user
from app.database.database import get_db as get_db_session

user_router = APIRouter(prefix="/users", tags=["Users"])

# ------------------------
# Schemas
# ------------------------
class UserProfile(BaseModel):
    id: int
    name: str
    email: EmailStr 
    avatar_url: str | None = None

    class Config:
        orm_mode = True

class UpdateUserProfile(BaseModel):
    name: str | None = None
    avatar_url: str | None = None

# ------------------------
# Routes
# ------------------------

# Get current logged-in user
@user_router.get("/me", response_model=UserProfile)
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

# Update current logged-in user
@user_router.put("/me", response_model=UserProfile)
async def update_current_user_profile(
    update: UpdateUserProfile,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user)
):
    if update.name:
        current_user.name = update.name
    if update.avatar_url:
        current_user.avatar_url = update.avatar_url
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user

# Optional: fetch another user by ID (admin use) TODO remove this and add it for another user if needed - Karthik
@user_router.get("/{user_id}", response_model=UserProfile)
async def get_user_profile(user_id: int, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Optional: list all users (admin only) TODO do tha same with this too --Karthik
@user_router.get("/", response_model=List[UserProfile])
async def list_all_users(db: Session = Depends(get_db_session)):
    users = db.query(User).all()
    return users

# Optional: delete a user (admin only) TODO same with this too --Karthik
@user_router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
