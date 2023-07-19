def employee_home(request):
    employee = Employee.objects.all()
    print(employee)