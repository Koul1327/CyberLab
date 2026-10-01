from app_fixed import app


def test_wrong_password():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/login",
            data={
                "username": "Alex",
                "password": "definitely-wrong",
            },
        )
        assert response.status_code == 401

        with client.session_transaction() as saved_session:
            assert "username" not in saved_session
            assert "role" not in saved_session


def test_user_login():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/login",
            data={
                "username": "Alex",
                "password": "alex-lab-password",
            },
        )
        assert response.status_code == 200

        with client.session_transaction() as saved_session:
            assert saved_session["username"] == "Alex"
            assert saved_session["role"] == "user"


def test_user_admin_denied():
    app.config["TESTING"] = True

    with app.test_client() as client:
        login_response = client.post(
            "/login",
            data={
                "username": "Alex",
                "password": "alex-lab-password",
            },
        )
        assert login_response.status_code == 200

        with client.session_transaction() as saved_session:
            assert saved_session["role"] == "user"

        admin_response = client.get("/admin")
        assert admin_response.status_code == 403


def test_admin_login():
    app.config["TESTING"] = True

    with app.test_client() as client:
        login_response = client.post(
            "/login",
            data={
                "username": "admin",
                "password": "admin-lab-password",
            },
        )
        assert login_response.status_code == 200

        with client.session_transaction() as saved_session:
            assert saved_session["username"] == "admin"
            assert saved_session["role"] == "admin"

        admin_response = client.get("/admin")
        assert admin_response.status_code == 200
        assert b"Admin panel" in admin_response.data
