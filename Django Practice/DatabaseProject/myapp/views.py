from django.shortcuts import render
from .forms import *
# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        stdata=studForm(request.POST)
        if stdata.is_valid():
            stdata.save()
            print("Your data has been saved!")
            msg="Your data has been saved!"
        else:
            print(stdata.errors)
            msg="Error!Something went wrong..."
    return render(request,'index.html',{'msg':msg})

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})