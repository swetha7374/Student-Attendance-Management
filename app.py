from database import create_database
from attendance import add_student, mark_attendance

create_database()

while True:
    print("\n===== Student Attendance Management System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")

        print(add_student(name, roll_no))

    elif choice == "2":
        roll_no = input("Enter roll number: ")
        status = input("Enter status (Present/Absent): ")

        print(mark_attendance(roll_no, status))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice")