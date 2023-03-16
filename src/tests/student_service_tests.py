import unittest
from repository.student_repository import *
from services.student_service import *
from domain.student import Student
from domain.exception_classes import *


class TestStudentServiceAdd(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.student_service = StudentService(self.student_repository)
        self.valid_student = Student("17", "Student17", "917")

    def test_list_size_after_add(self):
        self.student_service.add_student("17", "Student17", "917")
        students_list = self.student_service.get_students()
        self.assertEqual(len(students_list), 14, 'incorrect list size after add!')

    def test_already_existing_id_add_error(self):
        self.student_service.add_student("17", "Student17", "917")
        with self.assertRaises(IdAlreadyInRepositoryException):
            self.student_service.add_student("10", "Student11", "916")


class TestStudentRepositoryRemove(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.student_service = StudentService(self.student_repository)
        self.valid_student1 = Student("17", "Student17", "917")
        self.valid_student2 = Student("18", "Student18", "915")
        self.student_service.add_student("17", "Student17", "917")
        self.student_service.add_student("18", "Student18", "915")

    def test_list_size_after_remove(self):
        self.student_service.remove_student(self.valid_student1.student_id)
        students_list = self.student_service.get_students()
        self.assertEqual(len(students_list), 14, 'incorrect list size after remove!')

    def test_unable_to_remove_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.student_service.remove_student("14")


class TestStudentRepositoryUpdate(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.student_service = StudentService(self.student_repository)
        self.student_update = Student("17", "Student16", "915")
        self.invalid_student_update = Student("18", "Student18", "915")
        self.student_service.add_student("17", "Student17", "917")

    def test_list_size_after_update(self):
        self.student_service.update_student("17", "Student16", "915")
        students_list = self.student_service.get_students()
        self.assertEqual(len(students_list), 14, 'incorrect list size after update!')

    def test_unable_to_find_student_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.student_service.update_student("18", "Student18", "915")

if __name__ == '__main__':
    unittest.main()