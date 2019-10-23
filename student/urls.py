from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add-student/',views.add_student, name='add_student')
]