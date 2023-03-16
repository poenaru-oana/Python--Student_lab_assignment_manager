import unittest
from repository.grade_repository import *
from domain.grade import Grade
from domain.exception_classes import *


class TestGradeRepositoryAdd(unittest.TestCase):
    def setUp(self):
        self.grade_repository = GradeRepository()
        self.valid_grade = Grade("1", "3", "10")
        self.invalid_grade = Grade("1", "3", "7")

    def test_list_size_after_add(self):
        self.grade_repository.add(self.valid_grade)
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(len(grades_list), 1, 'incorrect list size after add!')

    def test_data_of_added_grade(self):
        self.grade_repository.add(self.valid_grade)
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(grades_list[0], self.valid_grade, 'data saved incorrectly!')

    def test_already_existing_id_add_error(self):
        self.grade_repository.add(self.valid_grade)
        with self.assertRaises(DuplicateKeyException):
            self.grade_repository.add(self.invalid_grade)


class TestGradeRepositoryRemove(unittest.TestCase):
    def setUp(self):
        self.grade_repository = GradeRepository()
        self.valid_grade1 = Grade("1", "3", "10")
        self.valid_grade2 = Grade("1", "4", "7")
        self.grade_repository.add(self.valid_grade1)
        self.grade_repository.add(self.valid_grade2)

    def test_list_size_after_remove(self):
        self.grade_repository.remove((self.valid_grade1.assignment_id, self.valid_grade1.student_id))
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(len(grades_list), 1, 'incorrect list size after remove!')

    def test_data_of_remaining_grade(self):
        self.grade_repository.remove((self.valid_grade1.assignment_id, self.valid_grade1.student_id))
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(grades_list[0], self.valid_grade2, 'incorrect grade deleted!')

    def test_unable_to_remove_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.grade_repository.remove("7")


class TestGradeRepositoryUpdate(unittest.TestCase):
    def setUp(self):
        self.grade_repository = GradeRepository()
        self.valid_grade = Grade("1", "3", None)
        self.grade_update = Grade("1", "3", "10")
        self.invalid_grade_update = Grade("1", "4", "7")
        self.grade_repository.add(self.valid_grade)

    def test_list_size_after_update(self):
        self.grade_repository.update(self.grade_update)
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(len(grades_list), 1, 'incorrect list size after update!')

    def test_data_of_updated_grade(self):
        self.grade_repository.update(self.grade_update)
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(grades_list[0], self.grade_update, 'grade not updated correctly!')

    def test_unable_to_find_grade_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.grade_repository.update(self.invalid_grade_update)


class TestGradeRepositoryGetGrade(unittest.TestCase):
    def setUp(self):
        self.grade_repository = GradeRepository()
        self.valid_grade1 = Grade("1", "3", "10")
        self.valid_grade2 = Grade("1", "4", "7")
        self.grade_repository.add(self.valid_grade1)
        self.grade_repository.add(self.valid_grade2)

    def test_size_of_grades_list(self):
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(len(grades_list), 2, 'incorrect size of returned list!')

    def test_data_of_returned_grades(self):
        grades_list = self.grade_repository.get_grades()
        self.assertEqual(grades_list[0], self.valid_grade1, 'first grade not returned correctly!')
        self.assertEqual(grades_list[1], self.valid_grade2, 'second grade not returned correctly!')

    def test_data_of_returned_grade(self):
        self.assertEqual(self.grade_repository.get_grade(self.valid_grade1.assignment_id, self.valid_grade1.student_id),
                         self.valid_grade1, 'grade not returned correctly!')

    def test_unable_to_find_grade_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.grade_repository.get_grade("2", "3")

if __name__ == '__main__':
    unittest.main()