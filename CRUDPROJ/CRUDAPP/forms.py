from django import forms 
from .models import StudentInfo

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ["name", "email", "proj_desc", "password"]


