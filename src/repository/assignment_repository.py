from domain.exception_classes import *


class AssignmentRepository:
    def __init__(self):
        """
        Assignment repository constructor. It initializes the place where assignments are stored which is a dictionary.
        """
        self.__assignments = {}

    def add(self, assignment):
        """
        This function adds an assignment into the repository providing the fact that another assignment with the same id doesn't exist
        :param assignment: an object of type Assignment
        :raises IdAlreadyInRepositoryException: in case that another assignment with the same id is already in the repository
        """
        if assignment.assignment_id in self.__assignments:
            raise IdAlreadyInRepositoryException("This ID is already in use!")
        self.__assignments[assignment.assignment_id] = assignment

    def remove(self, assignment_id):
        """
        This function removes an assignment from the repository providing the fact there exists one with the id given as a parameter
        :param assignment_id: a string representing the id of the assignment
        :raises IdNotInRepositoryException: in case there is no assignment with the searched id in the repository
        """
        if assignment_id not in self.__assignments:
            raise IdNotInRepositoryException("This assignment doesn't exist!")
        del (self.__assignments[assignment_id])

    def update(self, assignment):
        """
        This function updates an assignment's data with the passed parameter value
        :param assignment: an object of type Assignment
        :raises IdAlreadyInRepositoryException: in case there is no assignment with the same id as the assignment parameter
        """
        if assignment.assignment_id not in self.__assignments:
            raise IdNotInRepositoryException("This assignment doesn't exist!")
        self.__assignments[assignment.assignment_id] = assignment

    def get_assignment(self, assignment_id):
        """
        The function searches the repository and returns the assignment with the id passed as a parameter
        :param assignment_id: a string representing the id of the assignment
        :return: an object of type Assignment
        :raises IdDoesntExistInRepositoryException: in case there is no assignment with the searched id in the repository
        """
        if assignment_id not in self.__assignments:
            raise IdNotInRepositoryException("This assignment doesn't exist!")
        return self.__assignments[assignment_id]

    def get_assignments(self):
        """
        :return: A list of all the assignments from the repository
        """
        return list(self.__assignments.values())
