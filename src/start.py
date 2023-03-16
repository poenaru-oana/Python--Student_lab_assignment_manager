from repository.assignment_repository import AssignmentRepository
from repository.student_repository import StudentRepository
from repository.grade_repository import GradeRepository
from services.assignment_service import AssignmentService
from services.student_service import StudentService
from services.grade_service import GradeService
from ui.ui import Ui

student_repository = StudentRepository()
assignment_repository = AssignmentRepository()
grade_repository = GradeRepository()
student_service = StudentService(student_repository)
assignment_service = AssignmentService(assignment_repository)
grade_service = GradeService(grade_repository, assignment_repository, student_repository)
ui = Ui(student_service, assignment_service, grade_service)

ui.run_menu()
