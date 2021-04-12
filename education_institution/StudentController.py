from functions import read_file
from functions import save_lines
from Student import Student
from functions import get_integer
from functions import get_float
from functions import average

class StudentController():

    students = []

    def __init__(self, carpeta, matter_controller):
        self.matter_controller = matter_controller
        self.carpeta = carpeta+".\\files\\students.txt"
        ##Leer Estudiantes
        lines = read_file(self.carpeta)
        for line in lines:
            campos = line.split("|")
            matters = list(filter(bool, campos[4].split(";")))
            matters_student = []
            for matter in matters:
                split_matter = matter.split("-")
                new_matter = {}
                new_matter["matter"] = self.matter_controller.get_matter(split_matter[0])
                new_matter["notes"] = list(filter(bool, split_matter[1].split("^")))
                matters_student.append(new_matter)
            self.students.append(Student(campos[0],campos[1],campos[2],campos[3],matters_student))

    def menu(self):
        while True:
            option = input('''
        ******** Menu ********
    1. Ingresar Estudiante
    2. Buscar Estudiante
    3. Listar Estudiantes
    4. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_student()
            elif option == "2":
                self.find_student()
            elif option == "3":
                self.list_students()
            elif option == "4":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def new_student(self):
        '''Ingresa un nuevo Estudiante'''
        campos = []
        print("\nDatos del Estudiante:")
        id = get_integer("Identificación : ")
        if self.search_student(id):
            print("\n!Identificación ya Existe¡")
        else:
            campos.append(str(id))
            campos.append(str(get_integer("Código : ")))
            campos.append(input("Nombres : "))
            campos.append(input("Apellidos : "))
            ##Matricular
            print("Matricular Materias:")
            matters_student = self.add_matter([])
            campos.append(matters_student)
            self.students.append(Student(campos[0], campos[1], campos[2], campos[3], campos[4]))
            self.save_students()

    def search_student(self, id):
        finded = False
        for student in self.students:
            if(student.id == id):
                finded =  True
        return finded

    def find_student(self):
        search = get_integer("\nDigite la Identificación del estudiante a Buscar: ")
        find_student = None
        for index in range(0, len(self.students)):
            if(self.students[index].id == search):
                find_student = self.students[index]
        if find_student != None:
            self.menu_student(find_student, index)
        else:
            print("\nEstudiante No encontrado")

    def menu_student(self, student, index):
        print(student.__str__())
        while True:
            option = input('''
        ******** Menu ********
        Estudiante '''+ str(student.id)+" "+ student.full_name() +'''
    1. Matricular Materia al Estudiante
    2. Seleccionar Materia del Estudiante
    3. Listar Materias del Estudiante
    4. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                student = self.new_matter(student)
                self.students[index] = student
                self.save_students()
            elif option == "2":
                self.find_matter(student, index)
            elif option == "3":
                self.list_matters(student)
            elif option == "4":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def list_students(self, students = None):
        if students == None:
            students = self.students
        print("\nId".center(15) + "Codigo".center(15)+ "Nombre".center(35)+ "Prom".center(5))
        for student in students:
            print(""+str(student.id)[:15].ljust(15)+str(student.code)[:15].ljust(15)+student.full_name()[:35].ljust(35)+str(student.average())[:5].ljust(5))
    
    def add_matter(self, matters_student):
        self.matter_controller.list_matter()
        new_matter = {}
        while True:
            matter_option = input("Por favor Seleccione la materia a Matricular: ")
            matter = self.matter_controller.get_matter(matter_option)
            if matter == None:
                print("Error Materia no encontrada, Intente nuevamente ...")
                continue
            else:
                (f_matter, index2) = self.get_matter(matters_student, matter.id)
                if f_matter == None or index2 == -1:
                    new_matter["matter"] = matter
                    new_matter["notes"] = []
                    matters_student.append(new_matter)
                    while True:
                        option_repet = input("Desea Matricular más Materias (S/N) : ")
                        if (option_repet.lower()=="s" or option_repet.lower()=="n"):
                            break
                        else:
                            print("Opción No válida, Intente nuevamente ...")
                else:
                    print("Materia Ya Existe, por favor intente nuevamente")
                    continue
            if option_repet.lower() == "n":
                break
        return matters_student

    def new_matter(self, student):
        '''Ingresa una nueva Materia a un Estudiante'''
        print('''
            Ingresar Materia al Estudiante '''+ str(student.id)+" "+ student.full_name() )
        student.matters = self.add_matter(student.matters)
        return student

    def add_note(self, notes):
        while True:
            notes.append(str(get_float("Por favor Digite la nota a agregar: ")))
            while True:
                option_repet = input("Desea Ingresar otra Nota (S/N) : ")
                if (option_repet.lower()=="s" or option_repet.lower()=="n"):
                    break
                else:
                    print("Opción No válida, Intente nuevamente ...")
            if option_repet.lower() == "n":
                break
        return notes

    def menu_matter(self, student, index, matter, index2):
        print(student.__str__())
        while True:
            option = input('''
        ******** Menu ********
        Estudiante '''+ str(student.id)+" "+ student.full_name() +'''
        Materia '''+ str(matter["matter"].id)+" "+ matter["matter"].name +'''
    1. Ingresar Notas de la Materia
    2. Listar Notas de la Materia
    3. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                '''Agregar Notas a la Materia'''
                student.matters[index2]["notes"] = self.add_note(matter['notes'])
                self.students[index] = student
                self.save_students()
            elif option == "2":
                self.print_matter(matter)
            elif option == "3":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def find_matter(self, student, index):
        search = input("\nDigite el Id de la Materia Buscar: ")
        f_matter, index2 = self.get_matter(student.matters, search)
        if f_matter == None:
            print("!Materia no encontrada¡")
        else:
            self.print_matter(f_matter)
            self.menu_matter(student, index, f_matter, index2)

    def print_matter(self, f_matter):
        print(f_matter["matter"].__str__()+ '''
        Notas: {}
        Promedio: {} '''.format(", ".join(f_matter["notes"]),average(f_matter["notes"])))

    def get_matter(self, matters, id):
        find_matter = None
        i = -1
        for i in range(0, len(matters)):
            if(matters[i]["matter"].id == id):
                find_matter = matters[i]
                break
        return (find_matter, i)

    def list_matters(self, student, matters = None):
        if matters == None:
            matters = student.matters
        if len(matters)>0:
            sum_matter = 0
            print("\nCódigo".center(10) + "Nombre".center(30)+ "Promedio".center(5))
            for matter in matters:
                prom = average(matter["notes"])
                sum_matter += prom
                print(""+matter["matter"].id[:10].ljust(10)+matter["matter"].name[:30].ljust(30)+str(prom).rjust(5))
            print("Promedio General : ".center(40)+str(round(sum_matter/len(matters),2)).rjust(5))
        else:
            print("No Tiene Matriculado Ninguna Materia")

    def save_students(self):
        lines = []
        for student in self.students:
            list_matters = []
            for matter in student.matters:
                list_matters.append("{}-{}".format(matter["matter"].id,"^".join(matter["notes"])))
            lines.append("{}|{}|{}|{}|{}\n".format(student.id,student.code,student.name,student.last_name,";".join(list_matters)))
        save_lines(self.carpeta, lines)