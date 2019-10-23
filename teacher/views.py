from django.shortcuts import render,redirect
from .form import AddteacherForm
from .models import Teacher
from teacher.form import TeacherEditForm
from django.contrib.auth.models import User

# Create your views here.
def add_teacher(request):
    if request.method == 'GET':
        context = {
            'form': AddteacherForm()
        }
        return render(request,'teacher_create_dashboard.html', context)
    else:
        form = AddteacherForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id  # currently logged in user id
            data.save()
            return redirect('teacher_dashboard')
        else:
            return render(request, 'teacher_create_dashboard.html', {'form': form})


def delete_teacher(request,x):
    s = Teacher.objects.get(id=x)
    u = User.objects.get(id=s.user_id)
    u.delete()
    return redirect('manager_view')

def edit_teacher(request):
    if request.method == 'GET':
        return redirect('manager_view')
    else:
        a = Teacher.objects.get(user_id=request.user.id)
        e = TeacherEditForm(request.POST,None, instance=a)
        if e.is_valid():
            e.save()
        return redirect('manager_view')
