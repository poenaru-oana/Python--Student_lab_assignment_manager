import datetime

class Assignment:
    def __init__(self, assignment_id, description, deadline):
        self.__assignment_id = assignment_id
        self.__description = description
        self.__deadline = deadline

    @property
    def assignment_id(self):
        return self.__assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        self.__assignment_id = assignment_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline):
        self.__deadline = deadline

    def __eq__(self, other):
        return self.assignment_id == other.assignment_id and self.deadline == other.deadline and self.description == other.description

    def __str__(self):
        return "Assignment {}, Description: {}, Deadline: {}".format(self.__assignment_id, self.__description, self.__deadline.strftime('%d.%b.%Y'))
