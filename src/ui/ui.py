import traceback
from datetime import datetime
from services.undo_service import UndoableOperation
from services.undo_service import UndoService


class Ui:
    def __init__(self, student_service, assignment_service, grade_service):
        self.__student_service = student_service
        self.__assignment_service = assignment_service
        self.__grade_service = grade_service

    def print_menu_options(self):
        print("\n** MAIN MENU **",
              "\nasg - Assignments",
              "\nstud - Students",
              "\ngrd - Grade",
              "\nundo",
              "\nredo",
              "\nexit\n")

    def print_students_menu_options(self):
        print("\n** STUDENTS MENU **",
              "\n1. Add student",
              "\n2. Remove student",
              "\n3. Update student",
              "\n4. List all students"
              "\nback - return to Main Menu\n")

    def run_students_menu(self):
        while True:
            self.print_students_menu_options()
            students_option = input("Your option is: ")
            if students_option == 'back':
                return

            if students_option == '1':
                self.ui_add_student()
                continue
            if students_option == '2':
                self.ui_remove_student()
                continue
            if students_option == '3':
                self.ui_update_student()
                continue
            if students_option == '4':
                self.ui_list_students()
                continue

            raise Exception ("This option does not exist!")

    def print_assignments_menu_options(self):
        print("\n** ASSIGNMENTS MENU **",
              "\n1. Add assignment",
              "\n2. Remove assignment",
              "\n3. Update assignment",
              "\n4. List all assignments"
              "\nback - return to Main Menu\n")

    def run_assignments_menu(self):
        while True:
            self.print_assignments_menu_options()
            assignments_option = input("Your option is: ")
            if assignments_option == 'back':
                break

            if assignments_option == '1':
                self.ui_add_assignment()
                continue
            if assignments_option == '2':
                self.ui_remove_assignment()
                continue
            if assignments_option == '3':
                self.ui_update_assignment()
                continue
            if assignments_option == '4':
                self.ui_list_assignments()
                continue

            raise Exception("This option does not exist!")

    def print_grades_menu_options(self):
        print("\n** GRADES MENU **",
              "\n1. Give assignment to student",
              "\n2. Give assignment to group",
              "\n3. List ungraded assignments <provisory option>",
              "\n4. Grade an assignment"
              "\n5. Display all graded students with assignment"
              "\n6. Display late students"
              "\n7. Display graded students"
              "\nback - return to Main Menu\n")

    def run_grades_menu(self):
        while True:
            self.print_grades_menu_options()
            grades_option = input("Your option is: ")
            if grades_option == 'back':
                break

            if grades_option == '1':
                self.ui_add_assignment_to_student()
                continue
            if grades_option == '2':
                self.ui_add_assignment_to_group()
                continue
            if grades_option == '3':
                self.ui_list_ungraded_assignments()
                continue
            if grades_option == '4':
                self.ui_pick_and_grade_assignment()
                continue
            if grades_option == '5':
                self.ui_display_students_with_given_assignment_descending_by_grade()
                continue
            if grades_option == '6':
                self.ui_display_late_students()
                continue
            if grades_option == '7':
                self.ui_display_students_ordered_descending_by_school_situation()
                continue

            raise Exception("This option does not exist!")

    def ui_add_student(self):
        student_id = input('Student ID: ')
        name = input('Student Name: ')
        group = input('Student Group: ')

        self.__student_service.add_student(student_id, name, group)

    def ui_add_assignment(self):
        assignment_id = input('Assignment ID: ')
        description = input('Assignment Description: ')
        deadline = input('Assignment Deadline: ')

        try:
            deadline = datetime.strptime(deadline, '%d/%m/%Y')
        except Exception as exception:
            print("Wrong datetime format!")
            return

        self.__assignment_service.add_assignment(assignment_id, description, deadline)

    def ui_add_assignment_to_student(self):
        assignment_id = input('Assignment ID: ')
        student_id = input('Student ID: ')

        self.__grade_service.add_assignment_to_student(assignment_id, student_id)

    def ui_add_assignment_to_group(self):
        assignment_id = input('Assignment ID: ')
        group = input('Student Group: ')
        students = self.__student_service.get_students_in_group(group)

        self.__grade_service.add_assignment_to_students(assignment_id, students)

    def ui_remove_student(self):
        student_id = input('Student ID: ')

        self.__student_service.remove_student(student_id)
        self.__grade_service.remove_assignments_from_deleted_student(student_id)

    def ui_remove_assignment(self):
        assignment_id = input('Assignment ID: ')

        self.__assignment_service.remove_assignment(assignment_id)
        self.__grade_service.remove_deleted_assignment_from_students(assignment_id)

    def ui_update_student(self):
        student_id = input('Student ID: ')
        name = input('Student Name: ')
        group = input('Student Group: ')

        self.__student_service.update_student(student_id, name, group)

    def ui_update_assignment(self):
        assignment_id = input('Assignment ID: ')
        description = input('Assignment Description: ')
        deadline = input('Assignment Deadline: ')

        try:
            deadline = datetime.strptime(deadline, '%d/%m/%Y')
        except Exception as exception:
            print("Wrong datetime format!")
            return

        self.__assignment_service.update_assignment(assignment_id, description, deadline)

    def ui_list_students(self):
        for student in self.__student_service.get_students():
            print(student)

    def ui_list_assignments(self):
        for assignment in self.__assignment_service.get_assignments():
            print(assignment)

    def ui_list_ungraded_assignments(self):
        ungraded_assignments = self.__grade_service.get_ungraded_assignments()

        if ungraded_assignments != []:
            print("\nThe following assignments have not yet been graded:")
            for assignment in ungraded_assignments:
                print(assignment)
            return

        print("\nThere are no ungraded assignments at the moment.")

    def ui_grade_assignment(self):
        assignment_id = input('Assignment ID: ')
        student_id = input('Student ID: ')
        grade_value = input('Grade: ')

        self.__grade_service.grade_assignment(assignment_id, student_id, grade_value)

    def ui_pick_and_grade_assignment(self):
        ungraded_assignments = self.__grade_service.get_ungraded_assignments()
        self.ui_list_ungraded_assignments()
        if ungraded_assignments != []:
            self.ui_grade_assignment()

    def ui_display_students_with_given_assignment_descending_by_grade(self):
        if len(self.__grade_service.get_graded_assignments()) == 0:
            print("\nThere are no graded assignments at the moment.")
            return

        assignment_id = input("Assignment id: ")
        students_grades_list = self.__grade_service.get_students_ordered_descending_by_grade_on_given_assignment(assignment_id)

        if len(students_grades_list) == 0:
            print("\nThere are no students who handed in this assignment.")
            return

        for student_grade in students_grades_list:
            print("Name: {}, Grade: {}".format(student_grade[0], student_grade[1]))

    def ui_display_late_students(self):
        late_students = self.__grade_service.get_late_students()
        if len(late_students) == 0:
            print("\nNo students are late handing in their assignments.")
            return

        for student in late_students:
            print(student)

    def ui_display_students_ordered_descending_by_school_situation(self):
        if len(self.__grade_service.get_graded_assignments()) == 0:
            print("\nThere are no graded students at the moment.")
            return

        students_grades_list = self.__grade_service.get_students_ordered_descending_by_school_situation()

        for student_grade in students_grades_list:
            print("Name: {}, Grade: {}".format(student_grade[0], student_grade[1]))

    def run_menu(self):
        while True:
            self.print_menu_options()
            option = input(">>> ")

            if option == "exit":
                break
            try:
                if option == "stud":
                    self.run_students_menu()
                    continue
                if option == "asg":
                    self.run_assignments_menu()
                    continue
                if option == "grd":
                    self.run_grades_menu()
                    continue
                if option == "undo":
                    UndoService.undo()
                    continue
                if option == "redo":
                    UndoService.redo()
                    continue

                raise Exception("This option does not exist!")

            except Exception as exception:
                print('\n ', exception)
                traceback.print_exc()
