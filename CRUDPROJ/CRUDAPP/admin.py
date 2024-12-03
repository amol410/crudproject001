from django.contrib import admin
from .models import StudentInfo, Salary_of_Employee

# Register your models here.
# admin.site.register(StudentInfo)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "password"]

admin.site.register(StudentInfo, StudentInfoAdmin)

class Salary_of_EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "salary"]

admin.site.register(Salary_of_Employee, Salary_of_EmployeeAdmin)