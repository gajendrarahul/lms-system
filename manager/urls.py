from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('manager',views.manager_view,name='manager_view'),
    path('add-announcement/',views.add_announcement, name='add_announcement'),

]