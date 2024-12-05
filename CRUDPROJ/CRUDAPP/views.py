from django.shortcuts import render, HttpResponse, redirect
from .models import StudentInfo, Salary_of_Employee, UserClass
from CRUDAPP.forms import StudentRegistration
import hashlib

# Create your views here.
def crudapp(request):
    stu = StudentInfo.objects.all()
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # regi = StudentInfo(name="name", email="email", proj_desc="proj_desc", password="password")
            form.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()        
    return render(request, 'CRUDAPP/home.html', {'form':form, "stu":stu})

def salary(request):
    if request.method == 'GET':
        salary_info = Salary_of_Employee.objects.all().order_by('salary')[1]
    return render(request, 'CRUDAPP/salarypage.html', {'salary':salary_info})


def update_data(request, id):
    if request.method == 'POST':
        user_data = StudentInfo.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=user_data)
        if form.is_valid():
            form.save()
    else:
        user_data = StudentInfo.objects.get(pk=id)
        form = StudentRegistration(instance=user_data)
    return render(request, 'CRUDAPP/home.html', {'form':form, 'user_data':user_data})


def delete(request, id):
    if request.method == 'POST':
        user_data = StudentInfo.objects.get(pk=id)
        user_data.delete()
        return HttpResponse("Record has been Deleted")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if UserClass.objects.filter(username=username).exists():
            return HttpResponse("User already Exists")
        
        hashed_password = hash_password(password)

        UserClass.objects.create(username=username, password=hashed_password)

        return HttpResponse("Signup successful")
    return render(request, 'CRUDAPP/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        hashed_password = hash_password(password)

        user = UserClass.objects.filter(username = username, password = hashed_password).first()

        if user:
            request.session['user_id'] = user.id
            return redirect("home")
        return HttpResponse("Invalid Credentials")
    return render(request, "CRUDAPP/login.html")


def logout(request):
    if 'user.id' in request.session:
        del request.session['user_id']
    return redirect('login')    
