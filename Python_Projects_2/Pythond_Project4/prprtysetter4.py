class Employee:
    def __init__(self):
        self.__salary=salary=30000
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        self.__salary=value
emp=Employee()
emp.salary=40000
print(emp.salary)