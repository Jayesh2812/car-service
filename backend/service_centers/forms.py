from django import forms
from .models import ServiceCenter
class CenterSignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    phoneNo = forms.DecimalField(max_digits=10,decimal_places=0)

class CenterForm(forms.ModelForm):
    class Meta:
        model = ServiceCenter
        exclude =['user', 'phoneNo']


class CenterLogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)