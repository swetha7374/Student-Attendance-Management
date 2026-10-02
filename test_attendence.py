import unittest
from attendance import add_student, mark_attendance

class TestAttendance(unittest.TestCase):

    def test_add_student(self):
        result = add_student("Test Student", "TEST001")
        self.assertIn(result, [
            "Student added successfully",
            "Roll number already exists"
        ])

    def test_mark_attendance(self):
        result = mark_attendance("TEST001", "Present")
        self.assertEqual(result, "Attendance marked successfully")


if __name__ == "__main__":
    unittest.main()