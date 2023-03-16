class Student:
    def __init__(self, student_id, name, group):
        self.__student_id = student_id
        self.__name = name
        self.__group = group

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    def __str__(self):
        return "{}, Name: {}, Group: {}".format(self.__student_id, self.__name, self.__group)