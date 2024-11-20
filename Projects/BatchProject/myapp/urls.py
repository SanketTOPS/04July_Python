from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersignup/',views.usersignup),
    path('userlogout/',views.userlogout),
]
