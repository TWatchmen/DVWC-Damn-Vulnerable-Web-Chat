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
        conn.execute(query)

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        print("[+] User registered")
        conn.commit()
        conn.close()