from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    completed: bool

class TodoInDB(TodoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True