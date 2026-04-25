from app import app

def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

def test_message_key():
    client = app.test_client()
    response = client.get("/")

    data = response.get_json()

    assert "message" in data

