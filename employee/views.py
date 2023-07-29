from django.shortcuts import render ,redirect
from .models import Employee,Testimonial, Feedbackform

# Create your views here.
def employee_home(request):
    employee = Employee.objects.all()
    return render(request,"home.html",{"employee":employee})

def add_employee(request):

    error_message = ''
    if request.method=="POST":
        #data fetch
        emp_name = request.POST.get("emp_name")
        emp_salary = request.POST.get("emp_salary")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # validation
        
        if not emp_name:
             error_message = "Enter valid employee name"
             return render(request,"add_employee.html",{"error_message": error_message})
        
        #if any data validation so it is here
        #create object
        e = Employee()
        e.name = emp_name
        e.phone = emp_phone
        e.salary = emp_salary
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #save the object
        e.save()

        return redirect("/")
    return render(request,"add_employee.html",{"error_message": error_message})

def delete_employee(request,id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("/")

def update_employee(request,id):
        if request.method=="GET":
            employee = Employee.objects.get(id=id)
            return render(request,"update_employee.html",{"employee":employee})
        
        elif request.method=="POST":
            emp_name = request.POST.get("emp_name")
            emp_phone = request.POST.get("emp_phone")
            emp_salary = request.POST.get("emp_salary")
            emp_address = request.POST.get("emp_address")
            emp_working = request.POST.get("emp_working")
            emp_department = request.POST.get("emp_department")
                    # validation
            if not emp_name:
                error_message = "Enter valid employee name"
                return render(request,"add_employee.html",{"error_message": error_message})
            
            e = Employee.objects.get(id=id)
            e.name = emp_name
            e.phone = emp_phone
            e.salary = emp_salary
            e.address = emp_address
            e.department = emp_department
            if emp_working is None:
                e.working=False
            else:
                e.working=True
            e.save()
            return redirect("/")
                    
def testimonials(request):
     testimonial = Testimonial.objects.all()
     return render(request,"testimonials.html",{"testimonial":testimonial})

def feedback(request):
     if request.method=="POST":
          emp_email = request.POST.get("emp_email")
          emp_name = request.POST.get("emp_name")
          emp_feedback = request.POST.get("emp_feedback")

          feedback1 = Feedbackform()
          feedback1.email = emp_email
          feedback1.name = emp_name
          feedback1.feedback = emp_feedback
          feedback1.save()

     return render(request,"feedback.html",{})
     
