from functions import read_file
from functions import save_lines
from Doctor import Doctor
from functions import get_integer
from functions import get_date
from AppointmentController import AppointmentController
from PatientController import PatientController

class DoctorController():

    doctors = []

    def __init__(self, carpeta, schedule_controller):
        self.schedule_controller = schedule_controller
        self.carpeta = carpeta+"\\files\\doctors.txt"
        patient_controller = PatientController(carpeta, schedule_controller, self)
        self.appointment_controller = AppointmentController(carpeta, schedule_controller, self, patient_controller)

    def load(self):
        ##Leer Doctores
        self.doctors = []
        lines = read_file(self.carpeta)
        for line in lines:
            campos = line.split("|")
            schedule_doctor = []
            for time in list(filter(bool, campos[3].split(";"))):
                schedule_doctor.append(self.schedule_controller.get_schedule(time))
            self.doctors.append(Doctor(campos[0],campos[1],campos[2],schedule_doctor))

    def menu(self):
        self.appointment_controller.load()
        self.load()
        while True:
            option = input('''
        ******** Menu ********
    1. Ingresar Doctor
    2. Buscar Doctor
    3. Listar Doctores
    4. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_doctor()
            elif option == "2":
                self.find_doctor()
            elif option == "3":
                self.list_doctors()
            elif option == "4":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def new_doctor(self):
        '''Ingresa un nuevo Doctor'''
        campos = []
        print("\nDatos del Doctor:")
        id = get_integer("Identificación : ")
        if self.search_doctor(id):
            print("\n!Identificación ya Existe¡")
        else:
            campos.append(str(id))
            campos.append(input("Nombres : "))
            campos.append(input("Apellidos : "))
            ##Horarios
            print("Asignar Horarios:")
            schedule_doctor = self.add_schedule([])
            campos.append(schedule_doctor)
            self.doctors.append(Doctor(campos[0],campos[1],campos[2],campos[3]))
            self.save_doctors()

    def search_doctor(self, id):
        finded = False
        for doctor in self.doctors:
            if(doctor.id == id):
                finded =  True
        return finded

    def get_doctor(self, id):
        finded = None
        for doctor in self.doctors:
            if(doctor.id == id):
                finded = doctor
        return finded

    def find_doctor(self):
        search = get_integer("\nDigite la Identificación del profesor a Buscar: ")
        find_doctor = None
        for index in range(0, len(self.doctors)):
            if(self.doctors[index].id == search):
                find_doctor = self.doctors[index]
        if find_doctor != None:
            self.menu_doctor(find_doctor, index)
        else:
            print("\nDoctor No encontrado")

    def menu_doctor(self, doctor, index):
        print(doctor.__str__())
        while True:
            option = input('''
        ******** Menu ********
        Doctor '''+ str(doctor.id)+" "+ doctor.full_name() +'''
    1. Asignar Hora al Doctor
    2. Listar Horario asignado al Doctor
    3. Listar Citas X Fecha
    4. Atender Cita
    5. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                doctor = self.new_schedule(doctor)
                self.doctors[index] = doctor
                self.save_doctors()
            elif option == "2":
                self.list_schedule(doctor)
            elif option == "3":
                date_ = get_date("\nPor favor digite la fecha para filtrar las Citas: ")
                self.appointment_controller.print_by_doctor(doctor.id, date_)
            elif option == "4":
                #Buscar la cita 
                id = input("Por favor digite el Número de la Cita a atender: ")
                appointment = self.appointment_controller.get_appointment(id)
                if appointment == None:
                    print("Cita No encontrada")
                elif appointment.doctor.id == doctor.id:
                    ##Guardar la Nota
                    self.appointment_controller.set_description(id=appointment.id)
                else:
                    print("La Cita no está asignada al Doctor")
            elif option == "5":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def list_doctors(self, doctors = None):
        if doctors == None:
            doctors = self.doctors
        print("\nId".center(15) + "Nombre".center(35))
        for doctor in doctors:
            print(""+str(doctor.id)[:15].ljust(15)+doctor.full_name()[:35].ljust(35))
    
    def add_schedule(self, schedule_doctor):
        self.schedule_controller.list_schedule()
        while True:
            schedule_option = input("Por favor Digite la Hora a Asignar: ")
            schedule = self.schedule_controller.get_schedule(schedule_option)
            if schedule == None:
                print("Error Hora no encontrada, Intente nuevamente ...")
                continue
            else:
                (f_schedule, index2) = self.get_schedule(schedule_doctor, schedule.time)
                if f_schedule == None or index2 == -1:
                    schedule_doctor.append(schedule)
                    while True:
                        option_repet = input("Desea Asignar más Horas (S/N) : ")
                        if (option_repet.lower()=="s" or option_repet.lower()=="n"):
                            break
                        else:
                            print("Opción No válida, Intente nuevamente ...")
                else:
                    print("Hora Ya Existe, por favor intente nuevamente")
                    continue
            if option_repet.lower() == "n":
                break
        return sorted(schedule_doctor)

    def new_schedule(self, doctor):
        '''Ingresa una nueva Hora a un Doctor'''
        print('''
            Ingresar Hora al Doctor '''+ str(doctor.id)+" "+ doctor.full_name() )
        doctor.schedule = self.add_schedule(doctor.schedule)
        return doctor

    def get_schedule(self, schedule, time):
        find_schedule = None
        i = -1
        for i in range(0, len(schedule)):
            if(schedule[i].time == time):
                find_schedule = schedule[i]
                break
        return (find_schedule, i)

    def list_schedule(self, doctor, schedule_list = None):
        if schedule_list == None:
            schedule_list = doctor.schedule
        if len(schedule_list)>0:
            print("\nHora".center(10))
            for schedule in schedule_list:
                print(""+schedule.time.center(10))
        else:
            print("No Tiene Asignado Ningun Horario")

    def save_doctors(self):
        self.doctors = sorted(self.doctors)
        lines = []
        for doctor in self.doctors:
            list_schedule = []
            for schedule in doctor.schedule:
                list_schedule.append(schedule.time)
            lines.append("{}|{}|{}|{}\n".format(doctor.id,doctor.name,doctor.last_name,";".join(list_schedule)))
        save_lines(self.carpeta, lines)