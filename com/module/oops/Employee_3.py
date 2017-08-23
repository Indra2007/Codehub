class Employee_3:

    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'
        Employee_3.no_of_emps += 1

    # Regular method or instance method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return  cls(first, last, pay)

    # static method
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True

    # @classmethod
    # def today(cls):
    #     print("Construct a date from time.time()")
    #     t = _time.time()
    #     return cls.fromtimestamp(t)



emp_1 = Employee_3('Indra', 'Gupta', 60000)
emp_2 = Employee_3('Rashmi', 'Agrahari', 35000)


# emp_1.set_raise_amount(1.05)
#
# print(Employee_3.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# Employee_3.set_raise_amount(2.00)
#
# print(Employee_3.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


emp_str_1 = 'Indra-Gupta-65000'
emp_str_2 = 'Rashmi-Gupta-55000'
emp_str_3 = 'Bntu-Gupta-45000'

#first, last, pay = Employee_3.from_string(emp_str_3)
#new_emp_3 = Employee_3(first, last, pay)

new_emp_3 = Employee_3.from_string(emp_str_3)

print(new_emp_3.email)
print(new_emp_3.pay)

import datetime
my_date = datetime.date(2017, 8, 13)

print(Employee_3.is_workday(my_date))