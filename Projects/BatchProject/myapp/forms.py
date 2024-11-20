from django import forms
from .models import *


class signupform(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'