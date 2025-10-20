#Implemented by Karthik  Tamarapalli


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load env
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", ".env"))
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("SUPABASE_URL", "postgresql://user:password@host:port/dbname?sslmode=require") #TODO Do check if it is right and works fine !! -Karthik


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine)
Base = declarative_base()

#Now the dependency for the user.py

def get_db():
        db = SessionLocal()
        try:
                yield db 
        finally:
                db.close()
 

