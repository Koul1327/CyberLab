import sqlite3
from flask import Flask, request

app = Flask(__name__)

def create_db():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT)")
    db.executemany(
        "INSERT INTO products (name) VALUES (?)",
        [("Keyboard",), ("Mouse",), ("Monitor",)],
    )
    db.commit()
    return db

@app.route("/search")
def search():
    name = request.args.get("name", "")
    db = create_db()

    try:
        query = f"SELECT id, name FROM products WHERE name = '{name}'"
        rows = db.execute(query).fetchall()
        return {"products": rows}
    finally:
        db.close()
