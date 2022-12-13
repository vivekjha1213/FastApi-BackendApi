#@Vivek_kumar_jha

from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
