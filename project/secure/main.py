import os
import json
import base64
import sqlite3
from flask import Flask, render_template, request
from markupsafe import escape
from html_sanitizer import Sanitizer

database_fname = "users.db"


def convert_to_blob(img_b64: str | bytes) -> bytes:
    if isinstance(img_b64, str):
        return img_b64.encode()
    return img_b64


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
    users = cursor.executescript("SELECT * FROM users").fetchall()

    # Ensure all images are binary strings
    user_list = []
    for user in users:
        user["image"] = convert_to_blob(user["image"])
        user_list.append(user)

    return render_template("debug.html", users=user_list)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = Sanitizer().sanitize(request.form.get("email"))
        password = Sanitizer().sanitize(request.form.get("password"))

        # execute a parameterized SQL query to check if the user exists in the database
        cursor.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
        )
        user = cursor.fetchone()

        if user:
            # if the user exists, redirect to their dashboard
            return render_template(
                "secret.html",
                secret=user["secret"],
                image=convert_to_blob(user["image"]),
                name=user["name"],
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


import re


def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    match = re.match(pattern, email)

    return match is not None


def is_password_strong(password):
    # Minimum length requirement
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, digits, and special characters
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = re.search(r"[!@#$%^&*()\-_=+{}[\]|;:'\"<>,.?/~`]", password)

    if not has_uppercase or not has_lowercase or not has_digit or not has_special:
        return False

    # Check against common password list
    with open("wordlist.txt", "r") as file:
        common_passwords = file.read().splitlines()

    if password in common_passwords:
        return False

    return True


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = Sanitizer().sanitize(request.form.get("name"))
        email = Sanitizer().sanitize(request.form.get("email"))
        password = Sanitizer().sanitize(request.form.get("password"))

        if not email or not password or not name:
            return "Missing information!"

        if not is_password_strong(password):
            return "Password is too weak. Please choose a stronger password."

        if not is_valid_email(email):
            return "Invalid email. Please try again."

        cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
        db_email = cursor.fetchone()

        if db_email:
            return "User already registered <br/>" 'Go <a href="/login">Login</a> '

        # parameterized SQL query
        cursor.execute(
            "INSERT INTO users (name, email, password, secret, image) VALUES (?, ?, ?, 'your secret', '')",
            (name, email, password),
        )
        conn.commit()
        return "User signed up <br/>" 'Go <a href="/login">Login</a> '
    else:
        return render_template("signup.html")


@app.route("/general", methods=["GET"])
def general():
    user_names = cursor.execute("SELECT name FROM users").fetchall()
    print(user_names)
    return render_template("general.html", user_names=escape(user_names))


if __name__ == "__main__":
    # Uncomment here if you have problems
    # app.secret_key = "super secret key"
    # app.config["SESSION_TYPE"] = "filesystem"

    app.run(host="127.0.0.1", port=5000)
