class Rectangle:
    def __init__(self):
        self.__length=10
        self.__width=5
    @property
    def area(self):
        return self.__length*self.__width
r=Rectangle()
print(r.area)