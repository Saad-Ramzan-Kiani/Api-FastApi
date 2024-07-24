from typing import List
from models import TodoInDB, db
from schemas import TodoCreate, TodoUpdate


def some_function():
    return "Hello from some_function"


def create_todo(todo: TodoCreate) -> TodoInDB:
    new_todo = TodoInDB(
        id=len(db) + 1,
        title=todo.title,
        description=todo.description or "",
        completed=False
    )
    db.append(new_todo)
    return new_todo

def get_todos() -> List[TodoInDB]:
    return db

def get_todo_by_id(todo_id: int) -> TodoInDB:
    for todo in db:
        if todo.id == todo_id:
            return todo
    return None

def update_todo(todo_id: int, todo: TodoUpdate) -> TodoInDB:
    for index, existing_todo in enumerate(db):
        if existing_todo.id == todo_id:
            updated_todo = existing_todo.copy(update=todo.dict())
            db[index] = updated_todo
            return updated_todo
    return None

def delete_todo(todo_id: int) -> bool:
    for index, existing_todo in enumerate(db):
        if existing_todo.id == todo_id:
            del db[index]
            return True
    return False



