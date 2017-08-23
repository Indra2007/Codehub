from com.module.oops.inheritance.Person import Person

class Employee(Person):

    'Common base class for all employees'
    _empCount = 0

    # def __int__(self, name, id, age, salary, designation):
    #     Person.__init__(self, self.name, self.id, self.age)
    #     self._salary = salary
    #     self._designation = designation

    """This is another way to call the super class constructor or init method"""
    def __int__(self, *args, salary, designation):
        super(Person, self).__init__(*args)
        self._salary = salary
        self._designation = designation
        Employee._empCount += 1

    def __display_count__(self):
        return("Total Employee %d" % self.empCount)

    def __get_salary__(self):
        return self._salary

    def __get_designation__(self):
        return self._designation