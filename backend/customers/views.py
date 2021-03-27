from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required


from .models import Customer

from .forms import CustomerLoginForm, CustomerSignUpForm
# Create your views here.
User = get_user_model()

def login_view(request):
    form = CustomerLoginForm(request.POST or None)
    if form.is_valid():
        
        print(form.cleaned_data)
        user = authenticate(**form.cleaned_data)
        if user:
            if Customer.objects.filter(user = user):
                login(request, user)
                return redirect("customers:home")
    form = CustomerLoginForm()
    return render(request, 'customers/login.html', {'form' : form})

def signup_view(request):
    form = CustomerSignUpForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        phoneNo = form.cleaned_data.get('phoneNo')
        emailId = form.cleaned_data.get('emailId')

        user = User.objects.create_user(username = username, password = password)
        Customer.objects.create(user = user, phoneNo = phoneNo, emailId = emailId)

        return redirect('customers:login')

    form = CustomerSignUpForm()
    return render(request, 'customers/signup.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('customers:login')


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('customers:login')

    return render(request, 'customers/home.html')