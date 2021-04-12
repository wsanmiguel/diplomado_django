from Person import Person
from functions import average

class Student(Person):
    ##student = {
    ##    "id" = "1098626702",
    ##    "name" = "Wilson",
    ##    "last_name" = "Sanmiguel Guerrero"
    ##    "matters" = [
    ##        "id" = "1",
    ##        "name" = "Materia 1",
    ##        "notes" = [
    ##            1,2,3,4
    ##        ]
    ##    ]
    ##}
    
    def __init__(self, id, code, name, last_name, matters):
        Person.__init__(self, id, name, last_name)
        self.code = int(code)
        self.matters = matters

    def add_matter(self, matter):
        self.matters.append(matter)
    
    def average(self):
        sum = 0
        for matter in self.matters:
            sum += average(matter["notes"])
        return round(sum / len(self.matters), 2)
