from Person import Person

class Patient(Person):
    
    def __init__(self, id, name, last_name, appointments = []):
        Person.__init__(self, id, name, last_name)
        self.appointments = appointments

    def __gt__(self, student):
        return self.full_name() > student.full_name()
