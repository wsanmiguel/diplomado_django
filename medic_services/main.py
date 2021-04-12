'''1) Implementar la logica de una institucion educativa.

Profesores
Estudiantes
Materias
Notas
Horarios de Clase (*opcional)
estas entidades deben ser implementadas mediante objetos. el programa debe permitir las siguientes funciones:

1) un profesor debe poder ver las materias que tienen asignadas (un profesor puede dictar varias clases pero debe al menos dar una)
2) Una materia puede ser dictada por varios profesores y pueden estar inscritos varios estudiantes
3) un estudiante puede estar inscritos en muchas materias
4) las notas son ingresadas por el profesor que dicta la materia en la clase donde el estudiante este incrito
5) los estudiantes deben poder ver que notas tienen y ver un promedio por materia y general en todas sus materias
6) {OPCIONAL} - los horarios son definidos de maximo 6 horas diarias, un estudiante no puede estar en dos materias con el mismo horario, un profesor no puede dictar dos materias que sean vistas el mismo
'''
import os
print(os.getcwd())
from ScheduleController import ScheduleController
from PatientController import PatientController
from DoctorController import DoctorController
from AppointmentController import AppointmentController
carpeta = "D:\\Users\\sanmiguel\\Documents\\Diplomado django\\diplomado_django\\medic_services"

schedule = ScheduleController(carpeta)
doctor = DoctorController(carpeta, schedule)
patient = PatientController(carpeta, schedule, doctor)
appointment = AppointmentController(carpeta,schedule, doctor, patient)

while True:
    option = input('''
    ******** Menu ********
  1. Menu Pacientes
  2. Menu Doctores
  3. Menu Horarios
  4. Menu Citas
  5. Salir
  Por favor escoja su Opción: ''')
    if option == "1":
        patient.menu()
    if option == "2":
        doctor.menu()
    if option == "3":
        schedule.menu()
    if option == "4":
        appointment.menu()
    if option == "5" :
        break
    else:
        print("Opción no Válida, Por favor intentente Nuevamente\n")
