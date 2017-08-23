class Account:
    def __init__(self, initial):
        self.balance = initial
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def getBalance(self):
        return self.balance

a = Account(1000.00)
a.deposit(550.23)
a.deposit(100)
a.withdraw(50)

print("My Account balance is: ", a.getBalance())
