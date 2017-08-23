class Account(object):

    __slots__ = 'name', 'balance'  # Note: a tuple (‘name’,’balance’)

    "A simple class"

    # A class variable
    num_accounts = 0
    def __init__(self, name, balance):
        "Initialize the new Account Balance"
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self, amount):
        "Add to the balance"
        self.balance = self.balance + amount

    def withdraw(self, amount):
        "Subtract from the balance"
        self.balance = self.balance - amount

    def enquiry(self):
        "Return the current balance"
        return self.balance

account = Account('Indra', 10000.00)  # Invokes Account.__init__(account, 'Indra', 10000.00)
account_1 = Account('Rashmi', 5000.00) # Invokes Account.__init__(account_1, 'Indra', 10000.00)

account.deposit(5000.00)
account.withdraw(7000.00)

account_1.deposit(5000.00)
account_1.withdraw(3000.00)

# name = account.name
print('Total no. of accounts: ', account.num_accounts)

print(account.__dict__)
print(account_1.__dict__)

# print(Account.num_accounts)
# print(Account.__init__)
# print(Account.__del__)
# print(Account.deposit(1500))
# print(Account.withdraw(700))
# print(Account.enquiry())

# print(account)