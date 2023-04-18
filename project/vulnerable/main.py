import os
import json
import base64
import sqlite3
from flask import Flask, render_template, request

database_fname = "users.db"


def get_db_connection() -> sqlite3.Connection:
    # Check if the db already exists before creating it
    db_exists = os.path.isfile(database_fname)

    # Open connection
    db_connection = sqlite3.connect(database_fname, check_same_thread=False)

    # Fill sample data
    if not db_exists:
        with open("schema.sql") as db_schema:
            db_connection.executescript(db_schema.read())

        cur = db_connection.cursor()

        with open("sample_data/img.png", "rb") as img_file:
            img_b64 = base64.b64encode(img_file.read())

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
                    img_b64,
                ),
            )

        db_connection.commit()

    db_connection.row_factory = sqlite3.Row
    return db_connection


# Connect to sqlite database
conn = get_db_connection()

# Declare flask app
app = Flask(__name__, template_folder="templates")

# Create a cursor object
cursor = conn.cursor()


@app.route("/")
def index():
    # users = cursor.execute("SELECT * FROM users").fetchall()
    # return render_template("index.html", users=users)
    return render_template("index.html")

@app.route("/debug")
def debug():
    users = cursor.execute("SELECT * FROM users").fetchall()
    return render_template("debug.html", users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print("Email:", email)
        print("Password:", password)

        # execute an SQL query to check if the user exists in the database
        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password),
        )
        user = cursor.fetchone()

        if user:
            # if the user exists, redirect to their dashboard
            return render_template(
                "secret.html", secret=user["secret"], image=user["image"], name=user["name"]
            )
        else:
            # if the user doesn't exist, display an error message
            return (
                "Invalid email or password <br/>"
                'Go back to <a href="/login">Login</a> '
                'or <br/> <a href="/signup">Sign Up</a> Page'
            )
    else:
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password or not name:
            return "Missing information!"

        cursor.execute("SELECT email FROM users WHERE email=?", (email,))
        db_email = cursor.fetchone()

        if db_email or not email:
            return "User already registered <br/>" 'Go <a href="/login">Login</a> '
        else:
            cursor.execute(
                "INSERT INTO users (name, email, password, secret, image) VALUES (?, ?, ?, ?, ?)",
                (name, email, password, "your secret", b""),
            )
            conn.commit()
        return "User signed up <br/>" 'Go <a href="/login">Login</a> '
    else:
        return render_template("signup.html")


if __name__ == "__main__":
    # Uncomment here if you have problems
    # app.secret_key = "super secret key"
    # app.config["SESSION_TYPE"] = "filesystem"

    app.run(host="127.0.0.1", port=5000)
