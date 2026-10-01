from labs.auth_bypass.vulnerable.app import app as vulnerable_app
from labs.auth_bypass.fixed.app import app as fixed_app

def test_auth_bypass_vulnerable():
    vulnerable_app.config["TESTING"] = True

    with vulnerable_app.test_client() as client:
        login_response = client.post(
            "/login",
            data={
                "username": "admin",
                "password": "definitely-wrong",
            },
        )
        assert login_response.status_code == 200

        admin_response = client.get("/admin")
        assert admin_response.status_code == 200
        assert b"Admin panel" in admin_response.data


def test_auth_bypass_fixed():
    fixed_app.config["TESTING"] = True

    with fixed_app.test_client() as client:
        login_response = client.post(
            "/login",
            data={
                "username": "admin",
                "password": "definitely-wrong",
            },
        )
        assert login_response.status_code == 401

        with client.session_transaction() as saved_session:
            assert "username" not in saved_session
            assert "role" not in saved_session

        admin_response = client.get("/admin")
        assert admin_response.status_code == 403
