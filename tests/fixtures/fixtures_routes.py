from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.fixture
def mock_test_client(mocker):
    mocker.patch(
        "pymongo.collection.Collection.find",
        return_value=[
            {
                "_id": "6420c8fadcbf831171005cf1",
                "title": "test_title",
                "description": "test_description",
                "status": "test_status",
            }
        ],
    )
    mocker.patch(
        "pymongo.collection.Collection.find_one",
        return_value={
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        },
    )
    mocker.patch(
        "pymongo.collection.Collection.insert_one",
        return_value=mocker.Mock(inserted_id="6420c8fadcbf831171005cf1"),
    )
    mocker.patch(
        "pymongo.collection.Collection.update_one",
        return_value=mocker.Mock(modified_count=1),
    )
    mocker.patch(
        "pymongo.collection.Collection.delete_one",
        return_value=mocker.Mock(deleted_count=1),
    )
    mocker.patch(
        "pymongo.collection.Collection.delete_many",
        return_value=mocker.Mock(deleted_count=1),
    )
    return TestClient(app)
