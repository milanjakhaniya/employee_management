from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "address", "working", "department")
    list_editable = ("name", "phone", "address", "working")
    search_fields = ("name", "phone", "address","department")
    list_filter = ("id", "name", "phone", "address", "working", "department")



# Register your models here.
admin.site.register(Employee,EmployeeAdmin)