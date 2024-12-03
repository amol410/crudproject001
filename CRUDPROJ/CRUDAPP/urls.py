from django.urls import path 
from CRUDAPP import views

urlpatterns = [
    path('crudapp/', views.crudapp, name='crudapp'),
    path('salary/', views.salary, name='salary')
]
