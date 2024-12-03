from django.shortcuts import render
from .models import StudentInfo, Salary_of_Employee
from CRUDAPP.forms import StudentRegistration

# Create your views here.
def crudapp(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # regi = StudentInfo(name="name", email="email", proj_desc="proj_desc", password="password")
            form.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()        
    return render(request, 'CRUDAPP/home.html', {'form':form})

def salary(request):
    if request.method == 'GET':
        salary_info = Salary_of_Employee.objects.all().order_by('salary')[1]
    return render(request, 'CRUDAPP/salarypage.html', {'salary':salary_info})    