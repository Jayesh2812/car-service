from django import forms
from django.forms import ModelForm
from .models import Mechanic

class MechanicLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class MechanicSignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    phoneNo = forms.DecimalField(max_digits=10,decimal_places=0)
    emailId = forms.EmailField()

