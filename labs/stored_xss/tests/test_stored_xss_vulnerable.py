from labs.stored_xss.vulnerable.app import app, comments

def test_saved_script_is_not_escaped():
    app.config["TESTING"] = True
    comments.clear()

    try:
        with app.test_client() as client:
            client.post("/", data={"comment": "<script>alert(1)</script>"})

        with app.test_client() as visitor:
            response = visitor.get("/")
            page = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<script>alert(1)</script>" in page
    finally:
        comments.clear()
