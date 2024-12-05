from django.urls import path 
from CRUDAPP import views

urlpatterns = [
    path('crudapp/', views.crudapp, name='home'),
    path('salary/', views.salary, name='salary'),
    path('crudapp/<int:id>/', views.update_data, name='updatedata'),
    path('delete/<int:id>/', views.delete, name='deletedata'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
