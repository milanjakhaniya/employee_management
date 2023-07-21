from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.employee_home,name="employee_home"),
    path('add_employee/',views.add_employee,name="add_employee"),
    path('delete_employee/<int:id>/',views.delete_employee,name="delete_employee"),
    path('update_employee/<int:id>/',views.update_employee,name="update_employee"),
    path('testimonials/',views.testimonials,name="testimonials"),
    path('feedback/',views.feedback,name="feedback"),
]