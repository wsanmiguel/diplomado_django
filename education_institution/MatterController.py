from functions import read_file
from functions import save_file
from Matter import Matter

class MatterController():

    matters = []

    def __init__(self, carpeta):
        self.carpeta = carpeta+".\\files\\matters.txt"
        ##Leer Materias
        lines = read_file(self.carpeta)
        for line in lines:
            campos = line.split("|")
            self.matters.append(Matter(campos[0],campos[1]))

    def menu(self):
        while True:
            option = input('''
        ******** Menu ********
    1. Ingresar Materia
    2. Buscar Materia
    3. Listar Materias
    4. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_matter()
            elif option == "2":
                self.find_matter()
            elif option == "3":
                self.list_matter()
            elif option == "4":
                break
            else:
                print("\nOpción no Válida, Por favor intentente Nuevamente")

    def get_matter(self, id):
        find_matter = None
        for matter in self.matters:
            if(matter.id == id):
                find_matter = matter
        return find_matter

    def new_matter(self):
        '''Ingresa una nueva Materia'''
        campos = []
        print("\nDatos de la Materia:")
        id = input("Id : ")
        find_matter = self.get_matter(id)
        if find_matter == None:
            campos.append(id)
            campos.append(input("Nombre : "))
            self.matters.append(Matter(campos[0], campos[1]))
            save_file(self.carpeta,'|'.join(campos)+"\n")
        else:
            print("\n!Id ya Existe¡")

    def find_matter(self):
        search = input("\nDigite el Nombre de la Materia Buscar: ")
        find_matters = []
        for matter in self.matters:
            if matter.name.lower().find(search.lower())>-1:
                find_matters.append(matter)
        if len(find_matters)>0:
            self.list_matter(find_matters)
        else:
            print("\nNo se ha encontrado ninguna materia")

    def list_matter(self, matters = None):
        if matters == None:
            matters = self.matters
        print("\nCódigo".center(10) + "Nombre".center(30))
        for matter in matters:
            print(""+matter.id[:10].ljust(10)+matter.name[:30].ljust(30))
    