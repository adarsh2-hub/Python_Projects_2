class Student:
    def __init__(self,marks):
        self.__marks=marks
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,value):
        self.__marks=value
student=Student(80)
print(student.marks)
student.marks=90
print(student.marks)