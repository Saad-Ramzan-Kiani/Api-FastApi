
from typing import List
from pydantic import BaseModel

class TodoInDB(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

# This will act as our in-memory "database"
db: List[TodoInDB] = []