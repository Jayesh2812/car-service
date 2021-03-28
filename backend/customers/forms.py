from django import forms
from django.forms import ModelForm
from .models import Customer
from mechanics.models import BookingRequest
class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class CustomerSignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    phoneNo = forms.DecimalField(max_digits=10,decimal_places=0)
    emailId = forms.EmailField()

class RequestForm(forms.ModelForm):
    class Meta:
        model=BookingRequest
        fields=['vehicleNumber','vehicleType','problemDescriptionByCustomer','locationState','locationCity','locationPinCode']

        # vehicleNumber.widget.attrs.update({'class': 'form-control'})