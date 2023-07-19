from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.employee_home,name="employee_home"),
    path('add_employee/',views.add_employee,name="add_employee"),
    path('delete_employee/<int:id>/',views.delete_employee,name="delete_employee")
]