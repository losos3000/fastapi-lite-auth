import os
import sqlite3


DB_PATH = "./example/database/example.db"


def check_db():
    if os.path.exists(DB_PATH):
        return True
    return False


def delete_db():
    if check_db():
        os.remove(DB_PATH)


def create_db():
    delete_db()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        passport_number TEXT NOT NULL UNIQUE,
        insurance_number TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    cursor.execute(
        "INSERT INTO user (full_name, phone, username, email, passport_number, insurance_number, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("Administrator" ,"000-00-00", "admin", "admin@example.com", "000000", "000-000", "admin")
    )

    cursor.execute(
        "INSERT INTO user (full_name, phone, username, email, passport_number, insurance_number, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("User", "123-45-67", "user", "user@example.com", "111222", "123-321", "user")
    )

    conn.commit()
    conn.close()
