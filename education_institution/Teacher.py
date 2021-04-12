from Person import Person
class Teacher(Person):
    def __init__(self, id, name, last_name, matters):
        Person.__init__(self, id, name, last_name)
        self.matters = matters