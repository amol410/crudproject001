from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    proj_desc = models.TextField()
    password = models.CharField(max_length=50)
