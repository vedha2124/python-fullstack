# Week 4 - todo API but now it actually saves to a database (sqlite)
# big difference from week 3: the data survives a restart now.
# run:  uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models

Base.metadata.create_all(bind=engine)   # makes the tables if they don't exist yet

app = FastAPI(title="Todo API with Database")


# gives each request a db session and makes sure it gets closed after
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserIn(BaseModel):
    name: str


class TodoIn(BaseModel):
    title: str


@app.post("/users")
def create_user(user: UserIn, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name)
    db.add(new_user)        # stage it
    db.commit()             # actually save it to the database
    db.refresh(new_user)    # get the new id back from the database
    return {"id": new_user.id, "name": new_user.name}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    result = []
    for user in users:
        result.append({"id": user.id, "name": user.name})
    return result


@app.post("/users/{user_id}/todos")
def create_todo(user_id: int, todo: TodoIn, db: Session = Depends(get_db)):
    # first make sure that user actually exists
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    new_todo = models.Todo(title=todo.title, owner_id=user_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return {
        "id": new_todo.id,
        "title": new_todo.title,
        "done": new_todo.done,
        "owner_id": new_todo.owner_id,
    }


@app.get("/users/{user_id}/todos")
def get_user_todos(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # user.todos works because of the relationship we set up in models.py
    result = []
    for todo in user.todos:
        result.append({"id": todo.id, "title": todo.title, "done": todo.done})
    return result


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}
