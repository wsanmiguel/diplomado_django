from functions import read_file
from functions import save_lines
from Patient import Patient
from Appointment import Appointment
from functions import get_integer
from functions import get_today
from functions import get_date
from functions import get_time

class AppointmentController():

    appointments = []

    def __init__(self, folder, schedule_controller, doctor_controller, patient_controller):
        self.folder = folder+"\\files\\appointments.txt"
        self.schedule_controller = schedule_controller
        self.patient_controller = patient_controller
        self.doctor_controller = doctor_controller

    def load(self):
        self.appointments = []
        ##Cargar los Pacientes
        self.patient_controller.load()
        ##Cargar los Doctores
        self.doctor_controller.load()
        ##Leer Citas
        lines = read_file(self.folder)
        for line in lines:
            campos = line.split("|")
            #Buscar el Doctor
            doctor = self.doctor_controller.get_doctor(int(campos[1]))
            #Buscar el Paciente
            patient = self.patient_controller.get_patient(int(campos[2]))
            self.appointments.append(Appointment(campos[0], doctor, patient, campos[3], campos[4], campos[5]))

    def menu(self):
        self.load()
        while True:
            option = input('''
        ******** Menu ********
    1. Agendar Cita
    2. Listar Todas las Citas
    3. Listar Citas X Fecha
    4. Listar Citas X Doctor
    5. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_appointment()
            elif option == "2":
                self.print_appointment()
            elif option == "3":
                self.print_by_date()
            elif option == "4":
                self.print_by_doctor()
            elif option == "5":
                break
            else:
                print("Opción no Válida, Por favor intentente Nuevamente\n")

    def get_appointment(self, id):
        finded = None
        for appointment in self.appointments:
            if(appointment.id == id):
                finded = appointment
        return finded

    def get_index_appointment(self, id):
        index = -1 
        for i in range(0, len(self.appointments)):
            if(self.appointments[i].id == id):
                index = i
        return index

    def appointment_patient(self, id):
        appointments = []
        for appointment in self.appointments:
            if appointment.patient.id == id:
                appointments.append(appointment)
        if len(appointments)>0:
            print("\nPaciente ya tiene Cita Agendada: \nId".center(10) + "Doctor".center(35)+ "Fecha".center(10)+ "Hora".center(5))
            for appointment in appointments:
                print(""+str(appointment.id)[:10].ljust(10)+str(appointment.doctor.full_name())[:35].ljust(35)+str(appointment.date_)[:10].ljust(10)+str(appointment.time_)[:5].ljust(5))

    def set_description(self, id=None, index=None):
        if index==None:
            if id == None:
                id = input("Por favor digite el Número de la Cita a atender: ")
            index = self.get_index_appointment(id)
            if index < 0:
                print("!Cita No encontrada¡...")
        if index >= 0:
            self.appointments[index].description = input("Por favor Digite la Nota de la Cita que va a atender: ")
            self.save_appointments()

    def appointment_doctor(self, id):
        appointments = []
        for appointment in self.appointments:
            if appointment.doctor.id == id:
                appointments.append(appointment)
        if len(appointments)>0:
            print("\nDoctor tiene las siguientes Citas Agendadas: \nId".center(10) + "Paciente".center(35)+ "Fecha".center(10)+ "Hora".center(5))
            for appointment in appointments:
                print(""+str(appointment.id)[:10].ljust(10)+str(appointment.patient.full_name())[:35].ljust(35)+str(appointment.date_)[:10].ljust(10)+str(appointment.time_)[:5].ljust(5))
    
    def available_date(self, doctor_id, patient_id, date_, time_):
        error = False
        for appointment in self.appointments:
            if appointment.date_ == date_ and appointment.time_ :
                if appointment.doctor.id == doctor_id :
                    print("\n!Error Fecha - Hora No se encuentra disponible¡")
                    error = True
                if appointment.patient.id == patient_id:
                    print("\n!Error Paciente ya tiene una Cita en la Fecha - Hora seleccionada¡")
                    error = True
        return error

    def new_appointment(self, patient = None):
        '''Ingresa una nueva Cita'''
        if patient == None :
            while True:
                id = get_integer("Identificación del Paciente: ")
                patient = self.patient_controller.get_patient(id)
                if(patient == None):
                    print("\n!Paciente No Encontrado¡")
                else:
                    print(patient.__str__())
                    break
        #Buscar Si El estudiante ya Tiene una Cita
        self.appointment_patient(patient.id)
        while True:
            id = get_integer("Identificación del Doctor: ")
            doctor = self.doctor_controller.get_doctor(id)
            if(doctor == None):
                print("\n!Doctor No Encontrado¡")
            else:
                print(doctor.__str__())
                break
        while True:
            date_ = get_date("Digite la Fecha de la Cita: ")
            time_ = get_time("Digite la Hora de la Cita: ")
            #Revisar si el paciente ya tiene una cita en la misma Hora
            #Revisar si el Doctor Tiene disponibilidad en la Hora
            if not self.available_date(doctor.id, patient.id, date_, time_):
                break
        self.appointments.append(Appointment(len(self.appointments)+1, doctor, patient, date_, time_))
        self.save_appointments()

    def print_by_date(self):
        date_ = get_date("\nImpresión de Citas X Fecha ")
        appointments = []
        for appointment in self.appointments:
            if appointment.date_ == date_:
                appointments.append(appointment)
        if len(appointments)>0:
            self.print_appointment(appointments)
        else:
            print("!No se encontraron Citas¡... ")

    def print_by_doctor(self, doctor_id=None, date_=None):
        print("\nImpresión de Citas X Doctor ")
        if doctor_id == None:
            doctor_id = get_integer("Por favor Digite la Identificación del Doctor: ")
        appointments = []
        for appointment in self.appointments:
            if appointment.doctor.id == doctor_id:
                if not date_==None:
                    if appointment.date_ == date_:
                        appointments.append(appointment)
                else:
                    appointments.append(appointment)
        if len(appointments)>0:
            self.print_appointment(appointments)
        else:
            print("!No se encontraron Citas¡... ")

    def print_by_patient(self, patient_id=None):
        if patient_id == None:
            print("\nImpresión de Citas X Paciente ")
            patient_id = get_integer("Por favor Digite la Identificación del Paciente: ")
        for appointment in self.appointments:
            if appointment.patient.id == patient_id:
                print( '''
                Doctor: {}
                Fecha: {} {}
                Descripción: {} '''.format(appointment.doctor.name, appointment.date_, appointment.time_, appointment.description))

    def print_appointment(self, appointment_list=None):
        if appointment_list == None:
            appointment_list = self.appointments
        print("\nId".center(11) + "Doctor".center(37)+ "Paciente".center(37)+ "Fecha".center(12)+ "Hora".center(6)+ "Nota".center(6))
        for appointment in appointment_list:
            print(""+str(appointment.id)[:10].ljust(11)+ 
                str(appointment.doctor.full_name())[:35].center(37)+
                str(appointment.patient.full_name())[:35].center(37)+
                str(appointment.date_)[:10].ljust(12)+
                str(appointment.time_)[:5].rjust(6)+
                str(appointment.get_attend())[:1].rjust(6))

    def save_appointments(self):
        lines = []
        for appointment in self.appointments:
            lines.append("{}|{}|{}|{}|{}|{}\n".format(appointment.id,appointment.doctor.id,appointment.patient.id,appointment.date_,appointment.time_, appointment.description))
        save_lines(self.folder, lines)