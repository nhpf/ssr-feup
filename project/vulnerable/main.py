import os
import json
import base64
import sqlite3
from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__, template_folder="templates")


conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store user information if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 password TEXT)''')

conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    #conn = get_db_connection()
    users = cursor.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("signup.html", users=users)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # execute an SQL query to check if the user exists in the database
        #conn = get_db_connection()
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cur.fetchone()
        
        if user:
            # if the user exists, redirect to their dashboard
            flash('Login successful')
            conn.close()
            return redirect(url_for('index'))
        else:
            # if the user doesn't exist, display an error message
            conn.close()
            return ('Invalid email or password <br/>'\
				'Go back to <a href="/login">Login</a> '\
				'or <br/> <a href="/signup">Sign Up</a> Page')
    else:
        return render_template('login.html')
    
    
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET' or request.method == 'POST':
    #conn = get_db_connection()
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        cur.execute("SELECT email FROM users WHERE email=?", (email,))
        dbemail = cur.fetchone()
        if dbemail or not email:
            return ('User already registered <br/>'\
                    'Go <a href="/login">Login</a> ')
        else:
            cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        return ('User signed up <br/>'\
                    'Go <a href="/login">Login</a> ')






if __name__ == "__main__":
    #if not os.path.isfile("database.db"):
     #   create_db_file()
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host = '127.0.0.1', port = 5000)
