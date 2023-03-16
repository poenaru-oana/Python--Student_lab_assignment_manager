from datetime import datetime
from services.undo_service import UndoableOperation
from services.undo_service import UndoService

from domain.grade import Grade
from domain.exception_classes import *


class GradeService:
    def __init__(self, grade_repository, assignment_repository, student_repository):
        self.__grade_repository = grade_repository
        self.__assignment_repository = assignment_repository
        self.__student_repository = student_repository

    def add_assignment_to_student(self, assignment_id, student_id):
        assignment = self.__assignment_repository.get_assignment(assignment_id)
        student = self.__student_repository.get_student(student_id)
        grade = Grade(assignment.assignment_id, student.student_id, None)
        self.__grade_repository.add(grade)
        UndoService.register_operation(UndoableOperation(
            lambda: self.__grade_repository.remove((assignment_id, student_id)),
            lambda: self.__grade_repository.add(grade)))

    def add_assignment_to_students(self, assignment_id, students):

        def undo_add_assignment_to_students():
            for student in students:
                try:
                    self.__grade_repository.remove((assignment_id, student.student_id))
                except:
                    continue

        def redo_add_assignment_to_students():
            for student in students:
                try:
                    assignment = self.__assignment_repository.get_assignment(assignment_id)
                    grade = Grade(assignment.assignment_id, student.student_id, None)
                    self.__grade_repository.add(grade)
                except:
                    continue

        redo_add_assignment_to_students()
        UndoService.register_operation(UndoableOperation(undo_add_assignment_to_students,
                                                         redo_add_assignment_to_students))

    def remove_assignments_from_deleted_student(self, student_id):
        grades = self.__grade_repository.get_grades()

        for grade in grades:
            if grade.student_id == student_id:
                grade_key = (grade.assignment_id, student_id)
                self.__grade_repository.remove(grade_key)

    def remove_deleted_assignment_from_students(self, assignment_id):
        grades = self.__grade_repository.get_grades()

        for grade in grades:
            if grade.assignment_id == assignment_id:
                grade_key = (assignment_id, grade.student_id)
                self.__grade_repository.remove(grade_key)

    def grade_assignment(self, assignment_id, student_id, grade_value):
        old_grade = self.__grade_repository.get_grade(assignment_id, student_id)
        if old_grade.grade_value is not None:
            raise ElementNotInListException("This assignment cannot be graded!")
        new_grade = Grade(assignment_id, student_id, grade_value)
        self.__grade_repository.update(new_grade)
        UndoService.register_operation(UndoableOperation(lambda: self.__grade_repository.update(old_grade),
                                                         lambda: self.__grade_repository.update(new_grade)))

    def get_students_ordered_descending_by_grade_on_given_assignment(self, assignment_id):
        assignment_grades = list(filter(lambda grade:
                                        grade.grade_value is not None
                                        and
                                        grade.assignment_id == assignment_id,
                                        self.get_grades()))

        assignment_grades.sort(key=lambda grade: grade.grade_value, reverse=True)

        students_grades_list = []
        for grade in assignment_grades:
            student = self.__student_repository.get_student(grade.student_id)
            students_grades_list.append((student.name, grade.grade_value))

        return students_grades_list

    def get_late_students(self):
        ungraded_assignments = self.get_ungraded_assignments()
        late_students = []

        for ungraded_assignment in ungraded_assignments:
            assignment = self.__assignment_repository.get_assignment(ungraded_assignment.assignment_id)
            if datetime.now().date() > assignment.deadline.date():
                student = self.__student_repository.get_student(ungraded_assignment.student_id)

                student_already_in_list = 0
                for stud in late_students:
                    if stud.student_id == student.student_id:
                        student_already_in_list = 1
                        break

                if not student_already_in_list:
                    late_students.append(student)

        return late_students

    def get_students_ordered_descending_by_school_situation(self):
        graded_assignments = self.get_graded_assignments()
        students = self.__student_repository.get_students()
        students_grades_list = []

        for student in students:
            student_grades = []
            for graded_assignment in graded_assignments:
                if graded_assignment.student_id == student.student_id:
                    student_grades.append(int(graded_assignment.grade_value))

            if len(student_grades):
                grade_sum = sum(student_grades)
                average_grade = grade_sum / len(student_grades)
                students_grades_list.append((student.name, average_grade))

        students_grades_list.sort(key=lambda student_grade: student_grade[1], reverse=True)
        return students_grades_list

    def get_grades(self):
        return self.__grade_repository.get_grades()

    def get_ungraded_assignments(self):
        return list(filter(lambda grade: grade.grade_value is None, self.get_grades()))

    def get_graded_assignments(self):
        return list(filter(lambda grade: grade.grade_value is not None, self.get_grades()))
