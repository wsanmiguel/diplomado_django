from functions import read_file
from functions import save_lines
from Patient import Patient
from functions import get_integer
from AppointmentController import AppointmentController

class PatientController():

    patients = []

    def __init__(self, carpeta, schedule_controller, doctor_controller):
        self.carpeta = carpeta+"\\files\\patients.txt"
        self.appointment_controller = AppointmentController(carpeta, schedule_controller, doctor_controller, self)

    def load(self):
        self.patients = []
        ##Leer Pacientes
        lines = read_file(self.carpeta)
        for line in lines:
            campos = line.split("|")
            self.patients.append(Patient(campos[0],campos[1],campos[2]))

    def menu(self):
        self.appointment_controller.load()
        self.load()
        while True:
            option = input('''
        ******** Menu ********
    1. Ingresar Paciente
    2. Buscar Paciente
    3. Listar Pacientes
    4. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_patient()
            elif option == "2":
                self.find_patient()
            elif option == "3":
                self.list_patients()
            elif option == "4":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def new_patient(self):
        '''Ingresa un nuevo Paciente'''
        campos = []
        print("\nDatos del Paciente:")
        id = get_integer("Identificación : ")
        if self.search_patient(id):
            print("\n!Identificación ya Existe¡")
        else:
            campos.append(str(id))
            campos.append(input("Nombres : "))
            campos.append(input("Apellidos : "))
            self.patients.append(Patient(campos[0], campos[1], campos[2]))
            self.save_patients()

    def search_patient(self, id):
        finded = False
        for patient in self.patients:
            if(patient.id == id):
                finded =  True
        return finded

    def get_patient(self, id):
        finded = None
        for patient in self.patients:
            if(patient.id == id):
                finded = patient
        return finded

    def find_patient(self):
        search = get_integer("\nDigite la Identificación del Paciente a Buscar: ")
        find_patient = None
        for index in range(0, len(self.patients)):
            if(self.patients[index].id == search):
                find_patient = self.patients[index]
        if find_patient != None:
            print(find_patient)
            #Listar Notas
            print("\nNotas del Paciente: ")
            self.appointment_controller.print_by_patient(search)
        else:
            print("\nPaciente No encontrado")

    def list_patients(self, patients = None):
        if patients == None:
            patients = self.patients
        print("\nId".center(15) + "Nombre".center(35))
        for patient in patients:
            print(""+str(patient.id)[:15].ljust(15)+patient.full_name()[:35].ljust(35))
    
    def save_patients(self):
        lines = []
        for patient in self.patients:
            list_appointments = []
            for appointment in patient.appointments:
                list_appointments.append(appointment.id)
            lines.append("{}|{}|{}\n".format(patient.id,patient.name,patient.last_name))
        save_lines(self.carpeta, lines)