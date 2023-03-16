import unittest
from repository.assignment_repository import *
from domain.assignment import Assignment
from domain.exception_classes import *


class TestAssignmentRepositoryAdd(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.valid_assignment = Assignment("10", "Lab10", "27/01/2021")
        self.invalid_assignment = Assignment("10", "Lab7", "22/01/2021")

    def test_list_size_after_add(self):
        self.assignment_repository.add(self.valid_assignment)
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(len(assignments_list), 1, 'incorrect list size after add!')

    def test_data_of_added_assignment(self):
        self.assignment_repository.add(self.valid_assignment)
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(assignments_list[0], self.valid_assignment, 'data saved incorrectly!')

    def test_already_existing_id_add_error(self):
        self.assignment_repository.add(self.valid_assignment)
        with self.assertRaises(IdAlreadyInRepositoryException):
            self.assignment_repository.add(self.invalid_assignment)


class TestAssignmentRepositoryRemove(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.valid_assignment1 = Assignment("10", "Lab10", "27/01/2021")
        self.valid_assignment2 = Assignment("9", "Lab9", "15/01/2021")
        self.assignment_repository.add(self.valid_assignment1)
        self.assignment_repository.add(self.valid_assignment2)

    def test_list_size_after_remove(self):
        self.assignment_repository.remove(self.valid_assignment1.assignment_id)
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(len(assignments_list), 1, 'incorrect list size after remove!')

    def test_data_of_remaining_assignment(self):
        self.assignment_repository.remove(self.valid_assignment1.assignment_id)
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(assignments_list[0], self.valid_assignment2, 'incorrect assignment deleted!')

    def test_unable_to_remove_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.assignment_repository.remove("7")


class TestAssignmentRepositoryUpdate(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.valid_assignment = Assignment("10", "Lab10", "27/01/2021")
        self.assignment_update = Assignment("10", "Lab9", "15/01/2021")
        self.invalid_assignment_update = Assignment("9", "Lab9", "15/01/2021")
        self.assignment_repository.add(self.valid_assignment)

    def test_list_size_after_update(self):
        self.assignment_repository.update(self.assignment_update)
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(len(assignments_list), 1, 'incorrect list size after update!')

    def test_data_of_updated_assignment(self):
        self.assignment_repository.update(self.assignment_update)
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(assignments_list[0], self.assignment_update, 'assignment not updated correctly!')

    def test_unable_to_find_assignment_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.assignment_repository.update(self.invalid_assignment_update)


class TestAssignmentRepositoryGetAssignment(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.valid_assignment1 = Assignment("10", "Lab10", "27/01/2021")
        self.valid_assignment2 = Assignment("9", "Lab9", "15/01/2021")
        self.assignment_repository.add(self.valid_assignment1)
        self.assignment_repository.add(self.valid_assignment2)

    def test_size_of_assignments_list(self):
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(len(assignments_list), 2, 'incorrect size of returned list!')

    def test_data_of_returned_assignments(self):
        assignments_list = self.assignment_repository.get_assignments()
        self.assertEqual(assignments_list[0], self.valid_assignment1, 'first assignment not returned correctly!')
        self.assertEqual(assignments_list[1], self.valid_assignment2, 'second assignment not returned correctly!')

    def test_data_of_returned_assignment(self):
        self.assertEqual(self.assignment_repository.get_assignment(self.valid_assignment1.assignment_id),
                         self.valid_assignment1, 'assignment not returned correctly!')

    def test_unable_to_find_assignment_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.assignment_repository.get_assignment("11")


if __name__ == '__main__':
    unittest.main()