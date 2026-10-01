class Car:
    def __init__(self):
        self.__speed=0
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,value):
        self.__speed=value
car=Car()
car.speed=100
print(car.speed)