from domain.exception_classes import *


class StudentRepository:
    def __init__(self):
        """
        Student repository constructor. It initializes the place where students are stored which is a dictionary.
        """
        self.__students = {}

    def add(self, student):
        """
        This function adds a student into the repository providing the fact that another student with the same id doesn't exist

        :param student: an object of type Student
        :raises IdAlreadyInRepositoryException: in case that another student with the same id is already in the repository
        """
        if student.student_id in self.__students:
            raise IdAlreadyInRepositoryException("This ID is already in use!")
        self.__students[student.student_id] = student

    def remove(self, student_id):
        """
        This function removes a student from the repository providing the fact there exists one with the id given as a parameter
        :param student_id: a string representing the id of the student
        :raises IdNotInRepositoryException: in case there is no student with the searched id in the repository
        """
        if student_id not in self.__students:
            raise IdNotInRepositoryException("This student doesn't exist!")
        del (self.__students[student_id])

    def update(self, student):
        """
        This function updates a student's data with the passed parameter value
        :param student: an object of type Student
        :raises IdNotInRepositoryException: in case there is no student with the same id as the student parameter
        """
        if student.student_id not in self.__students:
            raise IdNotInRepositoryException("This student doesn't exist!")
        self.__students[student.student_id] = student

    def get_student(self, student_id):
        """
        The function searches the repository and returns the student with the id passed as a parameter
        :param student_id: a string representing the id of the student
        :return: an object of type Student
        :raises IdNotInRepositoryException: in case there is no student with the searched id in the repository
        """
        if student_id not in self.__students:
            raise IdNotInRepositoryException("This student doesn't exist!")
        return self.__students[student_id]

    def get_students(self):
        """
        :return: A list of all the students from the repository
        """
        return list(self.__students.values())
