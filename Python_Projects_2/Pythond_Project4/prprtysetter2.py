class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        self.__balance=value
BK=BankAccount(5000)
print(BK.balance)
BK.balance=7500
print(BK.balance)