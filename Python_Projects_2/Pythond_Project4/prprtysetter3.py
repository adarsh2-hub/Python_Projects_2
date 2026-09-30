class Product:
    def __init__(self):
        self.__price=price=1000
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value>0:
            self.__price=value
        else:
            print("Price must be greater than 0..")
product=Product()
product.price=1500
print(product.price)