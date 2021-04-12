class Matter():
    def __init__(self, id, name):
        self.name = name
        self.id = id
    
    def __str__(self):
        return '''
        Identificación : {} 
        Nombre         : {} '''.format(self.id, self.name) 