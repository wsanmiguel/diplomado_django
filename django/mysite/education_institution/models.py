from django.db import models

# Create your models here.
#Grupos
#Materias
class Matter(models.Model):
    name = models.CharField(max_length=70)

#Terceros
class Third(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=90)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

#Profesor
class Teacher(Third):
    pass

class Group(models.Model):
    name = models.CharField(max_length=80)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.name)
    
#Estudiante
class Student(Third):
    code = models.IntegerField(primary_key=True)
    groups = models.ManyToManyField(Group)

#Materias Matriculadas de estudiantes
class Enrollment(models.Model):
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

#Notas de las Materias
class Score(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
