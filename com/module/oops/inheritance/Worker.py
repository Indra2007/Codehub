import com.module.oops.inheritance.Employee as Employee

class Worker(Employee):

    # def __init__(self, name, id, age, salary, designation, manager, workType):
    #     Employee.__init__(self, salary, designation)
    #     self._manager = manager
    #     self._workType = workType

    def __init__(self, *args, manager, workType):
        """It will call the super class constructor -- init method"""
        super(Employee, self).__init__(*args)
        self._manager = manager
        self._workType = workType

    def __get_work_type__(self):
        return self._workType

    def __get_manager__(self):
        return self._manager

