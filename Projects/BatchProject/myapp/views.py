from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def userlogin(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login successfully!")
            msg="Login successfully!"
            request.session['user']=unm
            return redirect('/')
        else:
            print("Error!Login faild...")
            msg="Error!Login faild..."
    return render(request,'userlogin.html',{'msg':msg})

def usersignup(request):
    if request.method=='POST':
        newReq=signupform(request.POST)
        if newReq.is_valid():
            newReq.save()
            print("Signup Successfully!")
            return redirect('userlogin')
        else:
            print(newReq.errors)
    return render(request,'usersignup.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')