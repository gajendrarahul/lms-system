from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . form import CreateUserForm
from django.contrib.auth.models import User
from teacher.models import Teacher
from student.models import Student
from manager.models import Manager,Announcement
from teacher.form import AddteacherForm
def home(request):
    return render(request, 'home.html')
def add_user(request):
    if request.method == 'GET':
        context = {
            'form': CreateUserForm(),
        }
        return render(request, 'register.html',context)
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request,'register.html',{'form': form})

def signin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            id = request.user.id
            x = checkteacherorstudent(id)
            if x == 1:
                return redirect('manager_view')
            elif x == 2:
                return redirect('teacher_dashboard')
            elif x == 3:
                return redirect('student_dashboard')
            else:
                return redirect('who')

        else:
            messages.error(request, 'Enter the valid username and password')
            return redirect('signin')
def signout(request):
    logout(request)
    return redirect('signin')

def teacher_dashboard(request):
    context ={
        'announcement':Announcement.objects.latest('id')
    }
    return render(request,'teacher_dashboard.html',context)

def student_dashboard(request):
    return render(request,'student_dashboard.html')
@login_required(login_url='signin')
def who(request):
    r = checkteacherorstudent(id=request.user.id)
    if r == 1:
        return redirect('manager_view')
    elif r == 2:
        return redirect('teacher_dashboard')
    elif r == 3:
        return redirect('student_dashboard')
    else:
        return render(request, 'who.html')

def checkteacherorstudent(id):
    try:
        m = Manager.objects.get(user_id=id)
        return 1
    except:
        try:
            a = Teacher.objects.get(user_id=id)
            return 2
        except:
            try:
                c = Student.objects.get(user_id=id)
                return 3
            except:
                return 4

def signout(request):
    logout(request)
    return redirect('signin')





