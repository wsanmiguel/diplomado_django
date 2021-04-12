from functions import read_file
from functions import save_lines
from Schedule import Schedule

class ScheduleController():

    def __init__(self, carpeta):
        self.carpeta = carpeta+"\\files\\schedule.txt"
        self.schedule_list = []
        ##Leer Horarios
        lines = read_file(self.carpeta)
        for line in lines:
            campos = line.split("|")
            self.schedule_list.append(Schedule(campos[0]))

    def menu(self):
        while True:
            option = input('''
        ******** Menu ********
    1. Ingresar Horario
    2. Listar Horarios
    3. Menú Anterior
    Por favor escoja su Opción: ''')
            if option == "1":
                self.new_schedule()
            elif option == "2":
                self.list_schedule()
            elif option == "3":
                break
            else:
                print("\nOpción no Válida, Por favor intentente Nuevamente")

    def get_schedule(self, time):
        find_schedule = None
        for schedule in self.schedule_list:
            if(schedule.time == time):
                find_schedule = schedule
        return find_schedule

    def new_schedule(self):
        '''Ingresa una nuevo Horario'''
        campos = []
        print("\nDatos del Horario:")
        time = input("Hora : ")
        find_schedule = self.get_schedule(time)
        if find_schedule == None:
            campos.append(time)
            self.schedule_list.append(Schedule(campos[0]))
            self.save_schedule()
        else:
            print("\n!Hora ya Existe¡")

    def list_schedule(self, schedule_list = None):
        if schedule_list == None:
            schedule_list = self.schedule_list
        print("\nHora".center(10) )
        for schedule in schedule_list:
            print(""+schedule.time[:10].center(10))

    def save_schedule(self):
        self.schedule_list = sorted(self.schedule_list)
        lines = []
        for schedule in self.schedule_list:
            lines.append("{}\n".format(schedule.time))
        save_lines(self.carpeta, lines)
    