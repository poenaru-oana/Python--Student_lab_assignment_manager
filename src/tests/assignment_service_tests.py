import unittest
from repository.assignment_repository import *
from services.assignment_service import *
from domain.assignment import Assignment
from domain.exception_classes import *


class TestAssignmentServiceAdd(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.assignment_service = AssignmentService(self.assignment_repository)
        self.valid_assignment = Assignment("10", "Lab10", "27/01/2021")

    def test_list_size_after_add(self):
        self.assignment_service.add_assignment("10", "Lab10", "27/01/2021")
        assignments_list = self.assignment_service.get_assignments()
        self.assertEqual(len(assignments_list), 8, 'incorrect list size after add!')

    def test_data_of_added_assignment(self):
        self.assignment_service.add_assignment("10", "Lab10", "27/01/2021")
        assignments_list = self.assignment_service.get_assignments()
        self.assertEqual(assignments_list[7], self.valid_assignment, 'data saved incorrectly!')

    def test_already_existing_id_add_error(self):
        self.assignment_service.add_assignment("10", "Lab10", "27/01/2021")
        with self.assertRaises(IdAlreadyInRepositoryException):
            self.assignment_service.add_assignment("10", "Lab7", "22/01/2021")


class TestAssignmentRepositoryRemove(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.assignment_service = AssignmentService(self.assignment_repository)
        self.valid_assignment1 = Assignment("10", "Lab10", "27/01/2021")
        self.valid_assignment2 = Assignment("9", "Lab9", "15/01/2021")
        self.assignment_service.add_assignment("10", "Lab10", "27/01/2021")
        self.assignment_service.add_assignment("9", "Lab9", "15/01/2021")

    def test_list_size_after_remove(self):
        self.assignment_service.remove_assignment(self.valid_assignment1.assignment_id)
        assignments_list = self.assignment_service.get_assignments()
        self.assertEqual(len(assignments_list), 8, 'incorrect list size after remove!')

    def test_data_of_remaining_assignment(self):
        self.assignment_service.remove_assignment(self.valid_assignment1.assignment_id)
        assignments_list = self.assignment_service.get_assignments()
        self.assertEqual(assignments_list[7], self.valid_assignment2, 'incorrect assignment deleted!')

    def test_unable_to_remove_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.assignment_service.remove_assignment("8")


class TestAssignmentRepositoryUpdate(unittest.TestCase):
    def setUp(self):
        self.assignment_repository = AssignmentRepository()
        self.assignment_service = AssignmentService(self.assignment_repository)
        self.assignment_update = Assignment("10", "Lab9", "15/01/2021")
        self.invalid_assignment_update = Assignment("9", "Lab9", "15/01/2021")
        self.assignment_service.add_assignment("10", "Lab10", "27/01/2021")

    def test_list_size_after_update(self):
        self.assignment_service.update_assignment("10", "Lab9", "15/01/2021")
        assignments_list = self.assignment_service.get_assignments()
        self.assertEqual(len(assignments_list), 8, 'incorrect list size after update!')

    def test_data_of_updated_assignment(self):
        self.assignment_service.update_assignment("10", "Lab9", "15/01/2021")
        assignments_list = self.assignment_service.get_assignments()
        self.assertEqual(assignments_list[7], self.assignment_update, 'assignment not updated correctly!')

    def test_unable_to_find_assignment_error(self):
        with self.assertRaises(IdNotInRepositoryException):
            self.assignment_service.update_assignment("9", "Lab9", "15/01/2021")

if __name__ == '__main__':
    unittest.main()