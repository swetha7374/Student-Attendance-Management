import sqlite3

def create_database():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()