from django.contrib import admin
from .models import *

# Register your models here.
class signupData(admin.ModelAdmin):
    list_display=['id','created','firstname','lastname','username','city','state','mobile']

admin.site.register(userSignup,signupData)