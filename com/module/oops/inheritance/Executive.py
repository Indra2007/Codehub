import com.module.oops.inheritance.Employee as Employee

class Executive(Employee):

    # def __init__(self, name, id, age, salary, designation, yearlyBonus):
    #     Employee.__init__(self, self.salary, self.designation)
    #     self._yearlyBonus = yearlyBonus

    def __init__(self, *args, yearlyBonus):
        super(Employee, self).__init__(*args)
        self._yearlyBonus = yearlyBonus

    def __get_yearly_bonus__(self):
        return self._yearlyBonus
