
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI(title="Todo API")
class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: str
    done: bool
todos = []
next_id = 1
@app.get("/")
def home():
    return {"message": "Welcome! Open /docs to try the API."}


@app.post("/todos")
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = {"id": next_id, "title": todo.title, "done": False}
    todos.append(new_todo)
    next_id = next_id + 1
    return new_todo
@app.get("/todos")
def get_all_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = updated.title
            todo["done"] = updated.done
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")