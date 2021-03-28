from django.shortcuts import render, redirect, get_object_or_404
from customers.models import *
from service_centers.models import *
from mechanics.models import *
from django.db.models import Q
# Create your views here.
from django.contrib.auth import authenticate, login, get_user_model, logout


from .forms import CenterForm, CenterSignUpForm, CenterLogInForm
User = get_user_model()

def home(request):
    if not request.user.is_authenticated:
        return redirect('service_center:login')
    if not ServiceCenter.objects.filter(user = request.user):
        return redirect('service_center:login')
        
    serviceCenterObj= get_object_or_404(ServiceCenter, user = request.user)
    requestObjs=BookingRequest.objects.filter(requestedTo=serviceCenterObj)
    activeRequests=requestObjs.filter(requestState=0)
    inactiveRequests=requestObjs.filter(~Q(requestState=0))
    mechanics=Mechanic.objects.filter(serviceCenter=serviceCenterObj)
    print(activeRequests)
    context={
        'activerequests':activeRequests,
        'pastrequests':inactiveRequests,
        'mechanics':mechanics,
    }
    return render(request,'service_centers/home.html',context)

def signup_view(request):
    form = CenterSignUpForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        phoneNo = form.cleaned_data.get('phoneNo')

        user = User.objects.create_user(username = username, password = password)
        login(request, user)
        ServiceCenter.objects.create(user = user, phoneNo = phoneNo)

        return redirect('service_center:details')

    form = CenterSignUpForm()
    return render(request, 'service_centers/signup.html', {'form':form})

def details_view(request):

    center = get_object_or_404(ServiceCenter, user = request.user)
    form = CenterForm( request.POST or None, instance=center)
    if form.is_valid():
        form.save()
        return redirect('service_center:home')


    return render(request, 'service_centers/detailsForm.html', {'form':form})

def login_view(request):
    form = CenterLogInForm(request.POST or None)
    if form.is_valid():
        
        user = authenticate(**form.cleaned_data)
        if user:
            print(user)
            if ServiceCenter.objects.filter(user = user):
                login(request, user)
                return redirect("service_center:home")
    form = CenterLogInForm()
    return render(request, 'service_centers/login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('service_center:login')



