from django.contrib import admin
from django.urls import path
from .views import index, matters, students, teachers, list_thirds, get_third, list_groups, get_group

urlpatterns = [
    path('', index),
    path('matters', matters),
    path('list_thirds/<third>/', list_thirds),
    path('third/<third>/<id>/', get_third),
    path('students', students),
    path('teachers', teachers),
    path('list_groups', list_groups, name='list_groups'),
    path('group/<id>/', get_group, name='get_group'),
]