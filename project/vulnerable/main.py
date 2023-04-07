import os
import json
import sqlite3
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


def create_db_file(fill_sample_data: bool = True) -> None:
    db_connection = sqlite3.connect("database.db")
    with open("schema.sql") as db_schema:
        db_connection.executescript(db_schema.read())

    if fill_sample_data:
        cur = db_connection.cursor()

        with open("sample_data/img.png", "rb") as img_file:
            img_blob = img_file.read()

        with open("sample_data/users.json", "r", encoding="utf-8") as sample_data_file:
            sample_data = json.load(sample_data_file)

        for user_name in sample_data.keys():
            cur.execute(
                """INSERT INTO users (name, email, password, secret, image) VALUES (?, ?, ?, ?, ?)""",
                (
                    user_name,
                    sample_data[user_name]["email"],
                    sample_data[user_name]["password"],
                    sample_data[user_name]["secret"],
                    sqlite3.Binary(img_blob),
                ),
            )

    db_connection.commit()
    db_connection.close()


def get_db_connection() -> sqlite3.Connection:
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    if not os.path.isfile("database.db"):
        create_db_file()
