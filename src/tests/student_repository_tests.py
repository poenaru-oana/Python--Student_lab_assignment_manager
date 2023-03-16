import unittest
from repository.student_repository import *
from domain.student import Student
from domain.exception_classes import *


class TestStudentRepositoryAdd(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.valid_student = Student("10", "Student10", "911")
        self.invalid_student = Student("10", "Student11", "916")

    def test_list_size_after_add(self):
        self.student_repository.add(self.valid_student)
        students_list = self.student_repository.get_students()
        self.assertEqual(len(students_list), 1, 'incorrect list size after add!')

    def test_data_of_added_student(self):
        self.student_repository.add(self.valid_student)
        students_list = self.student_repository.get_students()
        self.assertEqual(students_list[0], self.valid_student, 'data saved incorrectly!')

    def test_already_existing_id_add_error(self):
        self.student_repository.add(self.valid_student)
        with self.assertRaises(IdAlreadyInRepositoryException):
            self.student_repository.add(self.invalid_student)


class TestStudentRepositoryRemove(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.valid_student1 = Student("10", "Student10", "911")
        self.valid_student2 = Student("9", "Student9", "917")
        self.student_repository.add(self.valid_student1)
        self.student_repository.add(self.valid_student2)

    def test_list_size_after_remove(self):
        self.student_repository.remove(self.valid_student1.student_id)
        students_list = self.student_repository.get_students()
        self.assertEqual(len(students_list), 1, 'incorrect list size after remove!')

    def test_data_of_remaining_student(self):
        self.student_repository.remove(self.valid_student1.student_id)
        students_list = self.student_repository.get_students()
        self.assertEqual(students_list[0], self.valid_student2, 'incorrect student deleted!')

    def test_unable_to_remove_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.student_repository.remove("7")


class TestStudentRepositoryUpdate(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.valid_student = Student("10", "Student10", "911")
        self.student_update = Student("10", "Student11", "912")
        self.invalid_student_update = Student("9", "Student9", "917")
        self.student_repository.add(self.valid_student)

    def test_list_size_after_update(self):
        self.student_repository.update(self.student_update)
        students_list = self.student_repository.get_students()
        self.assertEqual(len(students_list), 1, 'incorrect list size after update!')

    def test_data_of_updated_student(self):
        self.student_repository.update(self.student_update)
        students_list = self.student_repository.get_students()
        self.assertEqual(students_list[0], self.student_update, 'student not updated correctly!')

    def test_unable_to_find_student_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.student_repository.update(self.invalid_student_update)


class TestStudentRepositoryGetStudent(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.valid_student1 = Student("10", "Student10", "911")
        self.valid_student2 = Student("9", "Student9", "917")
        self.student_repository.add(self.valid_student1)
        self.student_repository.add(self.valid_student2)

    def test_size_of_students_list(self):
        students_list = self.student_repository.get_students()
        self.assertEqual(len(students_list), 2, 'incorrect size of returned list!')

    def test_data_of_returned_students(self):
        students_list = self.student_repository.get_students()
        self.assertEqual(students_list[0], self.valid_student1, 'first student not returned correctly!')
        self.assertEqual(students_list[1], self.valid_student2, 'second student not returned correctly!')

    def test_data_of_returned_student(self):
        self.assertEqual(self.student_repository.get_student(self.valid_student1.student_id),
                         self.valid_student1, 'student not returned correctly!')

    def test_unable_to_find_student_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.student_repository.get_student("11")

if __name__ == '__main__':
    unittest.main()