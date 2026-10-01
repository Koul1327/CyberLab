from flask import Flask, request, session
import html

app = Flask (__name__)
app.secret_key = "cyberlab-secret"

@app.route("/")
def home():
    return "<h1>CyberLab</h1><p>Welcome to the lab!</p>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session["username"] = username
        session["role"] = "admin" if username == "admin" else "user"
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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
