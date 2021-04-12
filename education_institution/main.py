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
from StudentController import StudentController
from TeacherController import TeacherController
from MatterController import MatterController
carpeta = "D:\\Users\\sanmiguel\\Documents\\Diplomado django\\diplomado_django\\education_institution"

matter = MatterController(carpeta)
student = StudentController(carpeta, matter)
teacher = TeacherController(carpeta, matter)

while True:
    option = input('''
    ******** Menu ********
  1. Menu Estudiantes
  2. Menu Profesores
  3. Menu Materias
  4. Salir
  Por favor escoja su Opción: ''')
    if option == "1":
        student.menu()
    if option == "2":
        teacher.menu()
    if option == "3":
        matter.menu()
    if option == "4" :
        break
    else:
        print("Opción no Válida, Por favor intentente Nuevamente\n")
