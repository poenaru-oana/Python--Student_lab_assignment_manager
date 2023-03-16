import unittest
from datetime import datetime

from repository.assignment_repository import *
from domain.assignment import Assignment
from domain.student import Student
from domain.grade import Grade
from domain.exception_classes import *


class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.assignment = Assignment("1", "some assignment", datetime.strptime("20/12/2021", '%d/%m/%Y'))

    def test_to_string(self):
        self.assertEqual(str(self.assignment), "Assignment 1, Description: some assignment, Deadline: 20.Dec.2021")

    def test_setter_id(self):
        self.assignment.assignment_id = 3
        self.assertEqual(self.assignment.assignment_id, 3)

    def test_setter_description(self):
        self.assignment.description = "some other description"
        self.assertEqual(self.assignment.description, "some other description")


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("1", "name", "915")

    def test_setter_id(self):
        self.student.student_id = 2
        self.assertEqual(self.student.student_id, 2)

    def test_setter_name(self):
        self.student.name = "name2"
        self.assertEqual(self.student.name, "name2")

    def test_setter_group(self):
        self.student.group = "916"
        self.assertEqual(self.student.group, "916")


class TestGrade(unittest.TestCase):
    def setUp(self):
        self.grade = Grade("1", "1", "9")

    def test_setter_assignment_id(self):
        self.grade.assignment_id = "2"
        self.assertEqual(self.grade.assignment_id, "2")

    def test_setter_student_id(self):
        self.grade.student_id = "2"
        self.assertEqual(self.grade.student_id, "2")

    def test_setter_grade(self):
        self.grade.grade_value = "10"
        self.assertEqual(self.grade.grade_value, 10)

    def test_to_str(self):
        self.assertEqual(str(self.grade), "Assignment Id: 1, Student Id: 1, Grade: 9")

if __name__ == '__main__':
    unittest.main()