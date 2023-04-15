import os
import json
import base64
import sqlite3
from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__, template_folder="templates")


def create_db_file(fill_sample_data: bool = True) -> None:
    db_connection = sqlite3.connect("database.db")
    with open("schema.sql") as db_schema:
        db_connection.executescript(db_schema.read())

    if fill_sample_data:
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
    db_connection.close()