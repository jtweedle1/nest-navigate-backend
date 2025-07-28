# This file defines Pydantic models that can 1. validate incoming data 2. control what data goes out in responses

# Imports
from pydantic import BaseModel, EmailStr
from datetime import datetime

# For when a user registers for the first tinme
class UserIn(BaseModel):
    email: EmailStr # EmailStr vs. str for better validation
    name: str
    password: str

# What's returned after creating or fetching a user; does NOT include password
class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    coins: int
    creation_date: datetime