# Week 4 - the database tables (SQLAlchemy models)
# one User can have many Todos. The relationship() lines let me jump between them
# e.g. user.todos gives all that user's todos, todo.owner gives the user back.

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    todos = relationship("Todo", back_populates="owner")


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    done = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))   # links a todo to its user
    owner = relationship("User", back_populates="todos")
