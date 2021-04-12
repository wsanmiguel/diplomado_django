class Schedule():
    def __init__(self, time):
        self.time = time
    
    def __str__(self):
        return '''Hora: {} '''.format(self.time) 

    def __gt__(self, schedule):
        return self.time > schedule.time