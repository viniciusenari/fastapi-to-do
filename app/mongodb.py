import re

import pydantic
from bson.objectid import ObjectId
from pymongo import MongoClient

from app.models import TodoItemModel


pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


class MongoDBClient:
    def __init__(self, connection_string: str):
        self.mongo_client = MongoClient(connection_string)
        self.db = self.mongo_client["todo-db"]["todo-items"]

    def get_all_items(self):
        return [
            {
                "id": item["_id"],
                "title": item["title"],
                "description": item["description"],
                "status": item["status"],
            }
            for item in self.db.find()
        ]

    def get_item_by_id(self, id: str):
        return self.db.find_one({"_id": ObjectId(id)}, {"_id": 0})

    def search_items(
        self, title: str = None, description: str = None, status: str = None
    ):
        title_regex = re.compile(f".*{title}.*") if title else None
        description_regex = re.compile(f".*{description}.*") if description else None

        search_query = {"$or": []}
        if title_regex:
            search_query["$or"].append({"title": {"$regex": title_regex}})
        if description:
            search_query["$or"].append({"description": {"$regex": description_regex}})
        if status:
            search_query["$or"].append({"status": status})

        search_result = self.db.find(search_query)
        return [
            {
                "id": item["_id"],
                "title": item["title"],
                "description": item["description"],
                "status": item["status"],
            }
            for item in search_result
        ]

    def create_item(self, item: TodoItemModel):
        result = self.db.insert_one(item.dict())
        return result.inserted_id

    def update_item(self, item_id: str, item: TodoItemModel):
        result = self.db.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
        return "Updated" if result.modified_count else "Not found"

    def delete_item(self, item_id: str):
        result = self.db.delete_one({"_id": ObjectId(item_id)})
        return "Deleted" if result.deleted_count else "Not found"

    def delete_all_items(self):
        result = self.db.delete_many({})
        return f"Deleted {result.deleted_count} items"
