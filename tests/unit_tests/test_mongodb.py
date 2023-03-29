from app.models import TodoItemModel


def test_mongodb_client_get_all_items(mongo_client):
    result = mongo_client.get_all_items()
    assert result == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_mongodb_client_get_item_by_id(mongo_client):
    result = mongo_client.get_item_by_id("6420c8fadcbf831171005cf1")
    assert result == {
        "title": "test_title",
        "description": "test_description",
        "status": "test_status",
    }


def test_mongodb_client_search_items(mongo_client):
    result = mongo_client.search_items(
        title="test_title",
        description="test_description",
        status="test_status",
    )
    assert result == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_mongodb_client_create_item(mongo_client):
    item = TodoItemModel(
        title="test_title",
        description="test_description",
        status="test_status",
    )
    result = mongo_client.create_item(item)
    assert result == "6420c8fadcbf831171005cf1"


def test_mongodb_client_update_item(mongo_client):
    item = TodoItemModel(
        title="test_title",
        description="test_description",
        status="test_status",
    )
    result = mongo_client.update_item("6420c8fadcbf831171005cf1", item)
    assert result == "Updated"


def test_mongodb_client_delete_item(mongo_client):
    result = mongo_client.delete_item("6420c8fadcbf831171005cf1")
    assert result == "Deleted"


def test_mongodb_client_delete_all_items(mongo_client):
    result = mongo_client.delete_all_items()
    assert result == "Deleted 1 items"
