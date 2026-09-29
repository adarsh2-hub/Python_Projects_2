class Person:
    def __init__(self):
        self.__name="Adarsh"
    @property
    def name(self):
        return self.__name    
p=Person()
print(p.name)