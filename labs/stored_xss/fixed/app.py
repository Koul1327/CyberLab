from flask import Flask, request, render_template

app = Flask(__name__)

comments = []

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        text = request.form.get("comment", "")
        comments.append(text)

    comments_html = ""

    return render_template("index.html", comments=comments)
