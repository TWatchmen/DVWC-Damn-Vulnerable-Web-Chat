import os
import sqlite3
from encodings import cp437

DB_PATH = "database/database.db"
SQL_PATH = "database/init.sql"

def init_database():
    if os.path.exists(DB_PATH):
        return

    conn = sqlite3.connect(DB_PATH)

    with open(SQL_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("[+] Database created.")

def register_db(username, password):
    conn = sqlite3.connect(DB_PATH)

    try:

        query = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
        register = conn.execute(query)
        if not register:
            return False
        else:
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

    finally:
        print("[+] User registered")
        conn.close()

def login_db(username, password):
    conn = sqlite3.connect(DB_PATH)

    try:
        query = "SELECT * FROM users WHERE username = ? AND password = ?"

        user = conn.execute(query,(username, password)).fetchone()
        if user:
            return True
        else:
            return False

    finally:
        print("[+] User login")
        conn.close()