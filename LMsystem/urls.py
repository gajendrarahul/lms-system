"""LMsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add-user/',views.add_user, name='add_user'),
    path('teacher/', include('teacher.urls')),
    path('signin/',views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('teacher-dashboard/',views.teacher_dashboard,name='teacher_dashboard'),
    path('student-dashboard/',views.student_dashboard, name='student_dashboard'),
    path('who/',views.who,name='who'),
    path('student/',include('student.urls')),
    path('manager/', include('manager.urls')),
    path('signout/', views.signout, name='signout'),


]
