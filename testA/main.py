
from fastapi import FastAPI, HTTPException
from schemas import TodoCreate, TodoUpdate, TodoInDB
from crud import some_function  # Replace 'some_function' with the actual functions or classes you need
import crud
from models import TodoInDB, db
from typing import List


import sys
print(sys.path)

app = FastAPI()

def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/todos/", response_model=TodoInDB)
def create_todo(todo: TodoCreate):
    return crud.create_todo(todo)

@app.get("/todos/", response_model=List[TodoInDB])
def read_todos():
    return crud.get_todos()

@app.get("/todos/{todo_id}", response_model=TodoInDB)
def read_todo(todo_id: int):
    todo = crud.get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoInDB)
def update_todo(todo_id: int, todo: TodoUpdate):
    updated_todo = crud.update_todo(todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@app.delete("/todos/{todo_id}", response_model=bool)
def delete_todo(todo_id: int):
    success = crud.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return success
