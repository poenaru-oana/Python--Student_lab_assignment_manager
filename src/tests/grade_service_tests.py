import unittest
from repository.assignment_repository import AssignmentRepository
from repository.student_repository import StudentRepository
from repository.grade_repository import GradeRepository
from services.assignment_service import AssignmentService
from services.student_service import StudentService
from services.grade_service import GradeService
from domain.grade import Grade
from domain.exception_classes import *


class TestGradeServiceAdd(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.assignment_repository = AssignmentRepository()
        self.grade_repository = GradeRepository()
        self.student_service = StudentService(self.student_repository)
        self.assignment_service = AssignmentService(self.assignment_repository)
        self.grade_service = GradeService(self.grade_repository, self.assignment_repository, self.student_repository)

        self.valid_grade = Grade("1", "3", "10")
        self.invalid_grade = Grade("1", "3", "7")

    def testAddToStudent(self):
        self.grade_service.add_assignment_to_student("1", "3")
        self.assertEqual(len(self.grade_repository.get_grades()), 1)





if __name__ == '__main__':
    unittest.main()