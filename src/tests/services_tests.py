from domain.assignment import Assignment
from domain.student import Student
from repository.assignment_repository import AssignmentRepository
from repository.student_repository import StudentRepository
from services.assignment_service import AssignmentService
from services.student_service import StudentService
from domain.exception_classes import *
import datetime


def get_assignment_repository():
    assignment_repo = AssignmentRepository()
    return assignment_repo


def test_add_assignment():
    assignment_repository = get_assignment_repository()
    assignment_service = AssignmentService(assignment_repository)

    assignment_id = "8"
    description = "lab4"
    deadline = datetime.datetime(2021, 12, 13)

    assignment_service.add_assignment(assignment_id, description, deadline)
    assert len(assignment_repository.get_assignments()) == 8
    assignment_from_repo = assignment_repository.get_assignment(assignment_id)
    assignment = Assignment(assignment_id, description, deadline)
    assert assignment_from_repo.description == assignment.description
    assert assignment_from_repo.deadline == assignment.deadline


def test_remove_assignment():
    assignment_repository = get_assignment_repository()
    assignment_service = AssignmentService(assignment_repository)

    assignment_id = '3'
    assignment_service.remove_assignment(assignment_id)
    assert len(assignment_repository.get_assignments()) == 6
    try:
        assignment_repository.get_assignment(assignment_id)
        assert False

    except IdNotInRepositoryException as exception:
        assert True


def test_update_assignment():
    assignment_repository = get_assignment_repository()
    assignment_service = AssignmentService(assignment_repository)

    assignment_id = "4"
    description = "lab4"
    deadline = datetime.datetime(2021, 12, 13)

    assignment_service.update_assignment(assignment_id, description, deadline)
    assert len(assignment_repository.get_assignments()) == 7
    assignment_from_repo = assignment_repository.get_assignment(assignment_id)
    assignment = Assignment(assignment_id, description, deadline)
    assert assignment_from_repo.description == assignment.description
    assert assignment_from_repo.deadline == assignment.deadline


def get_student_repository():
    empty_repo = StudentRepository()
    return empty_repo


def test_add_student():
    student_repository = get_student_repository()
    student_service = StudentService(student_repository)

    student_id = "14"
    name = "Student Fourteen"
    group = "915"

    student_service.add_student(student_id, name, group)
    assert len(student_repository.get_students()) == 14
    student_from_repo = student_repository.get_student(student_id)
    student = Student(student_id, name, group)
    assert student_from_repo.name == student.name
    assert student_from_repo.group == student.group


def test_remove_student():
    student_repository = get_student_repository()
    student_service = StudentService(student_repository)

    student_id = '3'
    student_service.remove_student(student_id)
    assert len(student_repository.get_students()) == 12
    try:
        student_repository.get_student(student_id)
        assert False

    except IdNotInRepositoryException as exception:
        assert True


def test_update_student():
    student_repository = get_student_repository()
    student_service = StudentService(student_repository)

    student_id = "4"
    name = "Student Four"
    group = "915"

    student_service.update_student(student_id, name, group)
    assert len(student_repository.get_students()) == 13
    student_from_repo = student_repository.get_student(student_id)
    student = Student(student_id, name, group)
    assert student_from_repo.name == student.name
    assert student_from_repo.group == student.group


def test_services():
    test_add_assignment()
    test_remove_assignment()
    test_update_assignment()
    test_add_student()
    test_remove_student()
    test_update_student()
