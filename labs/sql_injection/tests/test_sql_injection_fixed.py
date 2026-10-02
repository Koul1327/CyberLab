from labs.sql_injection.fixed.app import app

def test_sql_injection_returns_no_products():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get(
            "/search",
            query_string={"name": "' OR 1=1 -- "},
        )

    assert response.status_code == 200
    assert response.get_json()["products"] == []


def test_search_finds_product():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get(
            "/search",
            query_string={"name": "Mouse"},
        )

    assert response.status_code == 200
    assert response.get_json()["products"] == [[2, "Mouse"]]
