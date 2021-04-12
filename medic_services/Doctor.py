from Person import Person

class Doctor(Person):
    
    def __init__(self, id, name, last_name, schedule):
        Person.__init__(self, id, name, last_name)
        self.schedule = schedule

    def __gt__(self, student):
        return self.full_name() > student.full_name()

    def __str__(self):
        return Person.__str__(self)+'''
        Horario : {} '''.format(", ".join(self.get_schedule()))

    def get_schedule(self):
        schedule_list = []
        for schedule in self.schedule:
            schedule_list.append(schedule.time)
        return schedule_list