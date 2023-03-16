from domain.exception_classes import *


class GradeRepository:
    def __init__(self):
        self.__grades = {}

    def add(self, grade):
        grade_key = (grade.assignment_id, grade.student_id)

        if grade_key in self.__grades:
            raise DuplicateKeyException('This student has already been given this assignment!')
        self.__grades[grade_key] = grade

    def remove(self, grade_key):
        if grade_key not in self.__grades:
            raise IdNotInRepositoryException('This student has not been given this assignment!')

        del (self.__grades[grade_key])

    def update(self, grade):
        grade_key = (grade.assignment_id, grade.student_id)
        if grade_key not in self.__grades:
            raise IdNotInRepositoryException('This assignment cannot be graded!')

        self.__grades[grade_key] = grade

    def get_grade(self, assignment_id, student_id):
        grade_key = (assignment_id, student_id)
        if grade_key not in self.__grades:
            raise IdNotInRepositoryException("Assignment doesn't exist!")
        return self.__grades[grade_key]

    def get_grades(self):
        return list(self.__grades.values())