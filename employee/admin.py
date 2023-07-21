from django.contrib import admin
from .models import Employee,Testimonial,Feedbackform

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

class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "feedback")
    list_editable = ("email", "name", "feedback")
    search_fields = ("email", "name", "feedback")
    list_filter = ("email", "name")
    
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Testimonial)
admin.site.register(Feedbackform)