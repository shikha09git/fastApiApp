
from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    age: int
    grade: str
