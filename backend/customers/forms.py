from django import forms
from .models import Customer

class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class CustomerSignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    phoneNo = forms.DecimalField(max_digits=10,decimal_places=0)
    emailId = forms.EmailField()
