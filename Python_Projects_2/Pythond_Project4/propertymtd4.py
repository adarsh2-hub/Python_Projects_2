class BankAccount:
    def __init__(self):
        self.__balance=5000
    @property
    def balance(self):
        return self.__balance
ba=BankAccount()
print(ba.balance)