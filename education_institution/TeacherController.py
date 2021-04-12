from functions import read_file
from functions import save_lines
from Teacher import Teacher
from functions import get_integer

class TeacherController():

    teachers = []

    def __init__(self, carpeta, matter_controller):
        self.matter_controller = matter_controller
        self.carpeta = carpeta+".\\files\\teachers.txt"
        ##Leer Profesores
        lines = read_file(carpeta+"\\files\\teachers.txt")
        for line in lines:
            campos = line.split("|")
            matters_teacher = []
            for id in list(filter(bool, campos[3].split(","))):
                matters_teacher.append(self.matter_controller.get_matter(id))
            self.teachers.append(Teacher(campos[0],campos[1],campos[2],matters_teacher))

    def menu(self):
        while True:
            option = input('''
        ******** Menu ********
    1. Ingresar Profesor
    2. Buscar Profesor
    3. Listar Profesores
    4. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_teacher()
            elif option == "2":
                self.find_teacher()
            elif option == "3":
                self.list_teachers()
            elif option == "4":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def new_teacher(self):
        '''Ingresa un nuevo Profesor'''
        campos = []
        print("\nDatos del Profesor:")
        id = get_integer("Identificación : ")
        if self.search_teacher(id):
            print("\n!Identificación ya Existe¡")
        else:
            campos.append(str(id))
            campos.append(input("Nombres : "))
            campos.append(input("Apellidos : "))
            ##Matricular
            print("Asignar Materias:")
            matters_teacher = self.add_matter([])
            campos.append(matters_teacher)
            self.teachers.append(Teacher(campos[0],campos[1],campos[2],campos[3]))
            self.save_teachers()

    def search_teacher(self, id):
        finded = False
        for teacher in self.teachers:
            if(teacher.id == id):
                finded =  True
        return finded

    def find_teacher(self):
        search = get_integer("\nDigite la Identificación del profesor a Buscar: ")
        find_teacher = None
        for index in range(0, len(self.teachers)):
            if(self.teachers[index].id == search):
                find_teacher = self.teachers[index]
        if find_teacher != None:
            self.menu_teacher(find_teacher, index)
        else:
            print("\nProfesor No encontrado")

    def menu_teacher(self, teacher, index):
        print(teacher.__str__())
        while True:
            option = input('''
        ******** Menu ********
        Profesor '''+ str(teacher.id)+" "+ teacher.full_name() +'''
    1. Asignar Materia al Profesor
    2. Listar Materias asignadas al Profesor
    3. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                teacher = self.new_matter(teacher)
                self.teachers[index] = teacher
                self.save_teachers()
            elif option == "2":
                self.list_matters(teacher)
            elif option == "3":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def list_teachers(self, teachers = None):
        if teachers == None:
            teachers = self.teachers
        print("\nId".center(15) + "Nombre".center(35))
        for teacher in teachers:
            print(""+str(teacher.id)[:15].ljust(15)+teacher.full_name()[:35].ljust(35))
    
    def add_matter(self, matters_teacher):
        self.matter_controller.list_matter()
        while True:
            matter_option = input("Por favor Seleccione la materia a Asignar: ")
            matter = self.matter_controller.get_matter(matter_option)
            if matter == None:
                print("Error Materia no encontrada, Intente nuevamente ...")
                continue
            else:
                (f_matter, index2) = self.get_matter(matters_teacher, matter.id)
                if f_matter == None or index2 == -1:
                    matters_teacher.append(matter)
                    while True:
                        option_repet = input("Desea Asignar más Materias (S/N) : ")
                        if (option_repet.lower()=="s" or option_repet.lower()=="n"):
                            break
                        else:
                            print("Opción No válida, Intente nuevamente ...")
                else:
                    print("Materia Ya Existe, por favor intente nuevamente")
                    continue
            if option_repet.lower() == "n":
                break
        return matters_teacher

    def new_matter(self, teacher):
        '''Ingresa una nueva Materia a un Profesor'''
        print('''
            Ingresar Materia al Profesor '''+ str(teacher.id)+" "+ teacher.full_name() )
        teacher.matters = self.add_matter(teacher.matters)
        return teacher

    def get_matter(self, matters, id):
        find_matter = None
        i = -1
        for i in range(0, len(matters)):
            if(matters[i].id == id):
                find_matter = matters[i]
                break
        return (find_matter, i)

    def list_matters(self, teacher, matters = None):
        if matters == None:
            matters = teacher.matters
        if len(matters)>0:
            print("\nCódigo".center(10) + "Nombre".center(30))
            for matter in matters:
                print(""+matter.id[:10].ljust(10)+matter.name[:30].ljust(30))
        else:
            print("No Tiene Asignado Ninguna Materia")

    def save_teachers(self):
        lines = []
        for teacher in self.teachers:
            list_matters = []
            for matter in teacher.matters:
                list_matters.append(matter.id)
            lines.append("{}|{}|{}|{}\n".format(teacher.id,teacher.name,teacher.last_name,",".join(list_matters)))
        save_lines(self.carpeta, lines)