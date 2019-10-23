from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('add_teacher',views.add_teacher, name='add_teacher'),
    path('teacher/delete/<int:x>', views.delete_teacher, name='delete_teacher'),
    path('edit-teacher/',views.edit_teacher, name='edit_teacher'),

    ]