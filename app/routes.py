import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import APIRouter

from app.models import TodoItemModel
from app.mongodb import MongoDBClient


load_dotenv()
router = APIRouter()
mongo_connection_string = os.getenv("MONGO_CONNECTION_STRING")
mongo_client = MongoDBClient(mongo_connection_string)


@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@router.get("/items")
async def get_items():
    return mongo_client.get_all_items()


@router.post("/items")
async def create_item(item: TodoItemModel):
    return mongo_client.create_item(item)


@router.get("/items/{item_id}")
async def get_item(item_id: str):
    return mongo_client.get_item_by_id(item_id)


@router.put("/items/{item_id}")
async def update_item(item_id: str, item: TodoItemModel):
    return mongo_client.update_item(item_id, item)


@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    return mongo_client.delete_item(item_id)


@router.get("/search")
async def search_items(
    title: Optional[str] = None,
    description: Optional[str] = None,
    status: Optional[str] = None,
):
    return mongo_client.search_items(
        title=title, description=description, status=status
    )


@router.get("/todo")
async def get_todo():
    return mongo_client.search_items(status="todo")


@router.get("/inprogress")
async def get_inprogress():
    return mongo_client.search_items(status="inprogress")


@router.get("/done")
async def get_done():
    return mongo_client.search_items(status="done")


@router.delete("/delete_all")
async def delete_all():
    return mongo_client.delete_all_items()
