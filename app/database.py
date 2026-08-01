import os
import sqlite3

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

def register_db(username, password, color):
    conn = sqlite3.connect(DB_PATH)

    try:

        query = "INSERT INTO users (username, password, color) VALUES ('" + username + "', '" + password + "', '" + color + "')"
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

def get_user_color(username):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    user = conn.execute(
        "SELECT color FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    conn.close()

    if user:
        return user["color"]

    return "white"