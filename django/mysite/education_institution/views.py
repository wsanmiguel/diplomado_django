from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Matter, Student, Teacher, Third, Group

# Create your views here.
def matters(request):
    list_matters = Matter.objects.all()
    response = ''
    for matter in list_matters:
        response = response + ' ' + matter.name

    return HttpResponse(response)

def api_students(request):
    list_students = Student.objects.all()
    response = {}
    for student in list_students:
        print(student.first_name, student.last_name)
        response[student.id] = {
            'full name': '{} {}'.format(student.first_name, student.last_name),
        }
        enrollments = student.enrollment_set.all()
        student_enrollment = []

        for enrollment in enrollments:

            average_enrollment = 0
            notes = enrollment.note_set.all()
            for note in notes:
                average_enrollment = average_enrollment + note.value

            average_enrollment = average_enrollment / len(notes)
            student_enrollment.append(
                {
                    'name': enrollment.subject.name,
                    'average': average_enrollment
                }
            )

        response[student.id]['enrollments'] = student_enrollment

    return JsonResponse(response)

def list_thirds(request, third):
    thirds = Third
    if third == "student":
        thirds = Student
    elif third == "teacher":
        thirds = Teacher
    thirds_ = thirds.objects.all()
    context = {
        "thirds": thirds_
    }
    return render(request, 'thirds.html', context)
    
def get_third(request, third, id):
    thirds = Third
    if third == "student":
        thirds = Student
    elif third == "teacher":
        thirds = Teacher
    thirds_ = thirds.objects
    third = thirds_.filter(id=id).first()
    context = {
        "title": third,
        "third": third
    }
    return render(request, 'third.html', context)

def students(request):
    list_students = Student.objects.all()
    context = {
        "students": list_students
    }
    return render(request, 'students.html', context)

def teachers(request):
    list_teachers = Teacher.objects.all()
    context = {
        "teachers": list_teachers
    }
    return render(request, 'teachers.html', context)
    #return JsonResponse(response)

def index(request):
    print('hola')
    return render(request, 'home.html')


def list_groups(request):
    groups = Group.objects.all()
    context = {
        "title": "Listado de Grupos",
        "groups": groups
    }
    return render(request, 'groups.html', context)

def get_group(request, id):
    group = Group.objects.filter(id=id).first()
    students = group.student_set.all()
    context = {
        'title': group,
        'group': group,
        'students': students
    }
    return render(request, 'group.html', context)
