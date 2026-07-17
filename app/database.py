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