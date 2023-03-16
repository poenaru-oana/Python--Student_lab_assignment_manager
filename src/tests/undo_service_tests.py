import unittest
from services.undo_service import UndoableOperation
from services.undo_service import UndoService
from repository.student_repository import *
from services.student_service import *


class TestGrade(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.student_service = StudentService(self.student_repository)

    def test_undo_redo(self):
        with self.assertRaises(CannotUndoException):
            UndoService.undo()

        self.student_service.add_student("100", "name", "915")
        UndoService.undo()
        self.assertEqual(len(self.student_service.get_students()), 13)
        UndoService.redo()
        self.assertEqual(len(self.student_service.get_students()), 14)

        with self.assertRaises(CannotRedoException):
            UndoService.redo()


if __name__ == '__main__':
    unittest.main()