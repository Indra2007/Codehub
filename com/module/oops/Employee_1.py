class Employee_1:

    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'
        Employee_1.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
print(Employee_1.no_of_emps)

emp_1 = Employee_1('Indra', 'Gupta', 60000)
emp_2 = Employee_1('Rashmi', 'Agrahari', 35000)

print(Employee_1.no_of_emps)
# Employee_1.raise_amount = 1.05
#
# emp_1.raise_amount = 1.05
#
# print(emp_1.__dict__)
#
# print(Employee_1.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

