from flask import Flask, request

app = Flask(__name__)

comments = []

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        text = request.form.get("comment", "")
        comments.append(text)

    comments_html = ""

    for comment in comments:
        comments_html += "<p>" + comment + "</p>"

    return """
    <form method="POST">
        <input name="comment" placeholder="Комментарий">
        <button type="submit">Отправить</button>
    </form>
    """ + comments_html
