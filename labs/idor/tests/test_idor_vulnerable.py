from labs.idor.vulnerable.app import app

def test_idor_exposes_other_user_note():
    app.config["TESTING"] = True

    with app.test_client() as client:
        login_response = client.post(
            "/login",
            data={"username": "Alex", "password": "alex-lab-password"},
        )

        assert login_response.status_code == 200

        response = client.get("/notes/2")

        assert response.status_code == 200
        assert response.get_json()["owner"] == "Bob"
