from labs.idor.fixed.app import app

def test_owner_can_read_note():
    app.config["TESTING"] = True

    with app.test_client() as client:
        login_response = client.post(
            "/login",
            data={"username": "Alex", "password": "alex-lab-password"},
        )

        assert login_response.status_code == 200

        response = client.get("/notes/1")

        assert response.get_json()["owner"] == "Alex"
        assert response.status_code == 200

def test_other_user_note_denied():
    app.config["TESTING"] = True

    with app.test_client() as client:
        login_response = client.post(
            "/login",
            data={"username": "Alex", "password": "alex-lab-password"},
        )

        assert login_response.status_code == 200

        response = client.get("/notes/2")

        assert response.status_code == 403


def test_guest_cannot_read_note():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/notes/1")

    assert response.status_code == 401

def test_missing_note_return():
    app.config["TESTING"] = True

    with app.test_client() as client:
        login_response = client.post(
            "/login",
            data={"username": "Alex", "password": "alex-lab-password"},
        )

        response = client.get("/notes/999")

        assert response.status_code == 404
