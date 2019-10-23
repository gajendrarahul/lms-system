from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from teacher.form import AddteacherForm,TeacherEditForm
from teacher.models import Teacher
from student.models import Student
from .form import AnnouncementContentForm
from manager.models import Manager,Announcement
# Create your views here.
def manager_view(request):
    c = Manager.objects.get(user_id=request.user.id)

    context = {
        'tform': AddteacherForm(),
        'teacher':Teacher.objects.all()[:6][::-1],
        'tedit':TeacherEditForm(),
        'student':Student.objects.all()[:6],
        'announcementform':AnnouncementContentForm(),
        'announcement':Announcement.objects.filter(manager_id=c.id)
    }
    return render(request,'manager_dashboard.html',context)
def add_announcement(request):
    if request.method == 'GET':
        return render(request,'manager_dashboard.html')
    else:
        form = AnnouncementContentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            c = Manager.objects.get(user_id=request.user.id)
            data.manager_id=c.id
            data.save()
            return redirect('manager_view')



