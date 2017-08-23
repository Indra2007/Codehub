class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Indra', 'Gupta', 60000)
emp_2 = Employee('Rashmi', 'Agrahari', 35000)

# print('{} {}'.format(emp_1.first, emp_1.last))

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Indra'
# emp_1.last = 'Gupta'
# emp_1.email = 'Indra.Gupta@yahoo.com'
#
# emp_2.first = 'Rashmi'
# emp_2.last = 'Gupta'
# emp_2.email = 'Rashmi.Gupta@yahoo.com'

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

Employee.raise_amount = 1.05

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)