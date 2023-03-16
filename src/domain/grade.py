class Grade:
    def __init__(self, assignment_id, student_id, grade_value):
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def assignment_id(self):
        return self.__assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        self.__assignment_id = assignment_id

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, grade_value):
        self.__grade_value = int(grade_value)

    def __str__(self):
        if self.__grade_value is None:
            return "Assignment Id: {}, Student Id: {}".format(self.__assignment_id, self.__student_id)
        return "Assignment Id: {}, Student Id: {}, Grade: {}".format(self.student_id, self.__assignment_id,
                                                                     self.__grade_value)