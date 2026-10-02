from labs.stored_xss.fixed.app import app,comments

def test_saved_script_is_escaped():
    app.config["TESTING"] = True
    comments.clear()

    try:
        with app.test_client() as client:
            client.post("/", data={"comment": "<script>alert(1)</script>"})

        with app.test_client() as visitor:
            response = visitor.get("/")
            page = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<script>alert(1)</script>" not in page
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in page
    finally:
        comments.clear()

def test_regular_comment_is_saved():
    app.config["TESTING"] = True
    comments.clear()

    try:
        with app.test_client() as newby:
            newby.post("/", data={"comment": "Hello world"})


        with app.test_client() as visitor:
            response = visitor.get("/")
            page = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "Hello world" in page
    finally:
        comments.clear()
