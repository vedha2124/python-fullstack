# Week 4 - database setup
# this is the boilerplate bit - engine, session and Base that the other files import.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///todos.db"   # just a local sqlite file

# check_same_thread=False is needed for sqlite + fastapi (found this in the docs)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)   # each request gets its own session
Base = declarative_base()                  # our models inherit from this
