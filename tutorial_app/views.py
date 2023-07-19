from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    
    isActive = True
    if request.method=='POST':
        result = request.POST.get('check')
        print(result)
        if result is None:
            isActive=False
        else:
            isActive=True

    date = datetime.datetime.now()
    name = "Haresh Vegad"
    list_1 = [
        'python developer',
        'looking for job',
        'learning approach',
        'javaScript',
        ]

    dictionary = {
        "location" : "from surat",
        "course" : "python",
        "month" : 6,
        "name" : "Haresh Vegad",
    }

    data = {
        "date" : date,
        "isActive":isActive,
        "name" : name,
        "list_1" : list_1,
        "dictionary_data" : dictionary,
    }
    return render(request,"home.html",data)

def index(request):
    return render(request,"index.html",{})

def services(request):
    return render(request,"services.html",{})

def about(request):
    return render(request,"about.html",{})
