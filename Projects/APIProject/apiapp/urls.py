from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('getall/',views.getall),
]