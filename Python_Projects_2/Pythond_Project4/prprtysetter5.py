class Car:
    def __init__(self):
        self.__speed=0
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,value):
        if value>0:
            self.__speed=value
        else:
            print("Speed must be between 0 and 200..")
car=Car()
car.speed=100
print(car.speed)