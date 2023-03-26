from pydantic import BaseModel


class TodoItemModel(BaseModel):
    _id: str
    title: str
    description: str
    status: str
