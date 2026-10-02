import sqlite3
from datetime import date

def add_student(name, roll_no):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, roll_no) VALUES (?, ?)",
            (name, roll_no)
        )
        conn.commit()
        result = "Student added successfully"
    except sqlite3.IntegrityError:
        result = "Roll number already exists"

    conn.close()
    return result


def mark_attendance(roll_no, status):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    today = str(date.today())

    cursor.execute(
        "INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)",
        (roll_no, today, status)
    )

    conn.commit()
    conn.close()

    return "Attendance marked successfully"