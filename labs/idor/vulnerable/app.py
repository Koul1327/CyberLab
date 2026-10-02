from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, session
import html

app = Flask (__name__)
app.secret_key = "cyberlab-secret"

users = {
    "Alex": {
        "password_hash": generate_password_hash("alex-lab-password"),
        "role": "user",
    },
    "admin": {
        "password_hash": generate_password_hash("admin-lab-password"),
        "role": "admin"
    }
}

notes = {
    1: {"owner": "Alex", "text": "Секретные заметки Алекса"},
    2: {"owner": "Bob", "text": "Секретные заметки Боба"},
}

@app.route("/")
def home():
    return "<h1>CyberLab</h1><p>Welcome to the lab!</p>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = users.get(username)
        if user is None:
            return "Неверное имя пользователя или пароль", 401
        if not check_password_hash(user["password_hash"], password):
            return "Неверное имя пользователя или пароль", 401
        session["username"] = username
        session["role"] = user["role"]
        return f"<h1>Hello, {username}!</h1>"
    return """
    <h1>Login</h1>
    <form method="POST">
        <input name="username" placeholder="Username">
        <input name="password" type="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>
    """

@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        return "<h1>Acces denied!</h1>", 403
    return "<h1>Admin panel</h1>"

@app.route("/xss")
def xss():
    q = request.args.get("q", "")
    q = html.escape(q)
    return f"<h1>Search: {q}</h1>"

@app.route("/notes/<int:note_id>")
def get_note(note_id):
    if "username" not in session:
        return "Сначала авторизируйтесь", 401

    note = notes.get(note_id)

    if note is None:
        return "Заметка не найдена", 404

    return note

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
