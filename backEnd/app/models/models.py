from sqlalchemy import Column, Integer, String
from app.database.database import Base

class User(Base):
    __tablename__ = "profiles"  # matches your Supabase table

    id = Column(Integer, primary_key=True, index=True)       # should match "id" column TODO do edit  all this keeping the other table things in mind
    
    name = Column(String, nullable=True)                     # "name" column in Supabase
    email = Column(String, unique=True, index=True, nullable=True)  # "email" column
    avatar_url = Column(String, nullable=True)               # "avatar_url" column
    # If you have other columns in your Supabase table, add them here
    # e.g.
    # created_at = Column(DateTime, nullable=True)
    # updated_at = Column(DateTime, nullable=True)
