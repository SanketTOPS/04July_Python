from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from BatchProject import settings

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

            #Email Sending Code
            otp=random.randint(11111,99999)
            sub="Your One Time Password"
            msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 97247 99469 | sanket@tops-int.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['username']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            
            #send_mail(subject="Your One Time Password",message=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 97247 99469 | sanket@tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=['kishantoliya4@gmail.com','meetladva1684@gmail.com','kevalkotadiya509@gmail.com','pratixagoswami2000@gmail.com','k.p.jogi89@gmail.com','radhikapithadia123@gmail.com'])
            return redirect('userlogin')
        else:
            print(newReq.errors)
    return render(request,'usersignup.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user')
    return render(request,'contact.html',{'user':user})

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    return render(request,'profile.html',{'user':user})