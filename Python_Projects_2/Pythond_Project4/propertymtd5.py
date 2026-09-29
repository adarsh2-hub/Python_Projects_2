class Product:
    def __init__(self):
        self.__price=1000
    @property
    def price(self):
        return self.__price
p=Product()
print(p.price)