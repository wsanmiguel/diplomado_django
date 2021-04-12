from django.db import models

# Create your models here.
#Materias
class Matter(models.Model):
    name = models.CharField(max_length=70)

#Terceros
class Third(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=90)
    phone = models.CharField(max_length=50)

#Estudiante
class Student(Third):
    code = models.IntegerField(primary_key=True)

#Profesor
class Teacher(Third):
    pass

#Profesores Tutores de Materias
class Tutor(models.Model):
    matter_id = models.ForeignKey(Matter, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

#Materias Matriculadas de estudiantes
class Enrollment(models.Model):
    matter_id = models.ForeignKey(Matter, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

#Notas de las Materias
class Score(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    matter_id = models.ForeignKey(Matter, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
