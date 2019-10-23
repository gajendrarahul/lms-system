from django.shortcuts import render,redirect
from .form import AddstudentForm
# Create your views here.
def add_student(request):
    if request.method == 'GET':
        context ={
            'form': AddstudentForm(),
        }
        return render(request,'student_create_dashboard.html',context)
    else:
        form = AddstudentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('signin')
        else:
            return render(request,'student_create_dashboard.html', {'form': form})
