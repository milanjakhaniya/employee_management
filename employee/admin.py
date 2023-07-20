from django.contrib import admin
from .models import Employee,Testimonial

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "address", "working", "department")
    list_editable = ("name", "phone", "address", "working")
    search_fields = ("name", "phone", "address","department")
    list_filter = ("id", "name", "phone", "address", "working", "department")

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "testimonial", "picture", "rating")
    list_editable = ("name", "testimonial", "picture", "rating")
    search_fields = ("name", "testimonial", "picture", "rating")
    list_filter = ("name", "testimonial", "picture", "rating")

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Testimonial)