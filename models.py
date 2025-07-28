# Imports
from sqlalchemy import DateTime, Column, Integer, String
from datetime import datetime
from .database import Base

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True) #index=True speeds up search/filter on a column
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String) #TO-DO: hash passwords
    coins = Column(Integer, default=0)
    creation_date = Column(DateTime, default=datetime.timezone.utc)

