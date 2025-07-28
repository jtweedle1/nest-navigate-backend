# Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

 # Database Connection
engine = create_engine('sqlite:///orm.db')

Session = sessionmaker(bind=engine) # factory used to interact with db; uses engine as bridge to db
session = Session() # start a new session

Base = declarative_base() # class factory / blueprint for database tables
Base.metadata.create_all(engine) # creates database tables if they don't already exist