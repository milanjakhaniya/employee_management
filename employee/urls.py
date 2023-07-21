from django.urls import path
from .import views

urlpatterns = [
    path('',views.employee_home,name='home'),
    path('add_employee/',views.add_employee),
    path('delete_employee/<int:id>/',views.delete_employee),
    path('update_employee/<int:id>/',views.update_employee),
    path('testimonials/',views.testimonials),
    path('feedback/',views.feedback),
]