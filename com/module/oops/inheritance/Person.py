class Person(object):

    def __init__(self, name, id, age):
        self._name = name
        self._id = id
        self._age = age

    def __set_name__(self, name):
        self._name = name

    @property
    def __get_name__(self):
        return self._name

    def _set_id__(self, id):
        self._id = id

    @property
    def __get_id__(self):
        return self._id

    def _set_age__(self, age):
        self._age = age

    @property
    def __get_age__(self):
        return self._age

    def __str__(self):
        return "Name: " + self._name + ", Id: " + str(self._id) + ", Age: " + str(self._age)
        # return ('Name: ', self.name, 'Id: ', self.id, 'Age: ', self.age)

person = Person('Indra', 1010, 35)

print(person)

print('Name : ', person.__get_name__)
print('Id : ', person.__get_id__)
print('Age : ', person.__get_age__)