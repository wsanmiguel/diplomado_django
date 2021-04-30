from django.contrib import admin

# Register your models here.
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name')
    list_filter = ('id','first_name', 'last_name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name')
    list_filter = ('id','first_name', 'last_name')
