from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Hotel

# Create your views here.

def index(request):

    obj = Place.objects.all() # to access all the objects into the variable obj and place the objects in loop
    obj2 = Hotel.objects.all()
    
    return render(request, "index.html",{'result':obj,'newresult':obj2}) #pass value with a comma in dict

def home(request):
    name="India"
    return render(request,"home.html",{'obj':name})


def addition(request):   
    return render(request,"addition.html")

def results(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    res=num1+num2
    return render(request,"results.html",{'results':res})