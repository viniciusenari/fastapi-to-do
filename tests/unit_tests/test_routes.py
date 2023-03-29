def test_healthcheck(mock_test_client):
    response = mock_test_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_items(mock_test_client):
    response = mock_test_client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_create_item(mock_test_client):
    response = mock_test_client.post(
        "/items",
        json={
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        },
    )
    assert response.status_code == 200
    assert response.json() == "6420c8fadcbf831171005cf1"


def test_get_item(mock_test_client):
    response = mock_test_client.get("/items/6420c8fadcbf831171005cf1")
    assert response.status_code == 200
    assert response.json() == {
        "title": "test_title",
        "description": "test_description",
        "status": "test_status",
    }


def test_update_item(mock_test_client):
    response = mock_test_client.put(
        "/items/6420c8fadcbf831171005cf1",
        json={
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        },
    )
    assert response.status_code == 200
    assert response.json() == "Updated"


def test_delete_item(mock_test_client):
    response = mock_test_client.delete("/items/6420c8fadcbf831171005cf1")
    assert response.status_code == 200
    assert response.json() == "Deleted"


def test_search_items(mock_test_client):
    response = mock_test_client.get("/search?title=test_title")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_get_todo_items(mock_test_client):
    response = mock_test_client.get("/todo")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_get_inprogress_items(mock_test_client):
    response = mock_test_client.get("/inprogress")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_get_done_items(mock_test_client):
    response = mock_test_client.get("/done")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "6420c8fadcbf831171005cf1",
            "title": "test_title",
            "description": "test_description",
            "status": "test_status",
        }
    ]


def test_delete_all_items(mock_test_client):
    response = mock_test_client.delete("/delete_all")
    assert response.status_code == 200
    assert response.json() == "Deleted 1 items"
