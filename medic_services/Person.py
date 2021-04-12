class Person():
    def __init__(self, id, name, last_name):
        self.name = name.strip().lower().title()
        self.last_name = last_name.strip().lower().title()
        self.id = int(id)
    
    def full_name(self):
        return self.name+" "+self.last_name

    def __str__(self):
        return '''
        Identificación : {} 
        Nombre         : {} '''.format(self.id,self.full_name())