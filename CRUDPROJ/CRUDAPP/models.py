from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    proj_desc = models.TextField()
    password = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name

class Salary_of_Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()

class UserClass(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
