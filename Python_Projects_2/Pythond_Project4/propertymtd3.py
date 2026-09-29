class Student:
    def __init__(self):
        self.__marks=85
    @property
    def marks(self):
        return self.__marks
s=Student()
print(s.marks)