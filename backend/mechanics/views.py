from django.shortcuts import render,redirect
from customers.models import *
from service_centers.models import *
from mechanics.models import *
from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Mechanic

from .forms import MechanicLoginForm, MechanicSignUpForm
# Create your views here.
User = get_user_model()

def login_view(request):
    form = MechanicLoginForm(request.POST or None)
    if form.is_valid():
        
        print(form.cleaned_data)
        user = authenticate(**form.cleaned_data)
        if user:
            if Mechanic.objects.filter(user = user):
                login(request, user)
                return redirect("mechanic_home")
    form = MechanicLoginForm()
    return render(request, 'mechanics/login.html', {'form' : form})

def signup_view(request):
    form = MechanicSignUpForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        phoneNo = form.cleaned_data.get('phoneNo')
        emailId = form.cleaned_data.get('emailId')

        user = User.objects.create_user(username = username, password = password)
        Mechanic.objects.create(user = user, phoneNo = phoneNo, emailId = emailId)

        return redirect('mechanics:login')

    form = MechanicSignUpForm()
    return render(request, 'mechanics/signup.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.
def home(request):
    mechanicObj=Mechanic.objects.get(id=1)
    requestObjs=BookingRequest.objects.filter(assignedMechanic=mechanicObj)
    acceptedReq=requestObjs.filter(requestState=1)
    pastReq=requestObjs.filter(requestState=3)
    print(acceptedReq)
    context={
        'activerequests':acceptedReq,
        'pastrequests':pastReq,
    }
    return render(request,'mechanics/home.html',context)

def createBill(request,reqid):
    reqObj=BookingRequest.objects.get(id=reqid)
    if(request.method=="POST"):
        description=request.POST['problemSolved']
        cost=request.POST['cost']
        billObj=BillGenerated(associatedRequest=reqObj)
        billObj.problemResolved=description
        billObj.cost=int(cost)
        billObj.save()
        print(request.POST)
    billObjects=BillGenerated.objects.filter(associatedRequest=reqObj)
    totalBill=0
    for obj in billObjects:
        totalBill+=obj.cost
    reqObj.bill=totalBill
    reqObj.save()
    context={
        'reqid':reqid,
        'billObjects':billObjects,
        'totalBill':totalBill

    }
    return render(request,'mechanics/bill.html',context)

def requestCompleted(request,reqid):
    reqObj=BookingRequest.objects.get(id=reqid)
    reqObj.requestState=3
    reqObj.serviceCompleteTime=datetime.now()
    reqObj.save()
    return redirect('mechanic_home')

def assign_mechanic(request):
    import json
    data = json.loads(request.body)

    req_id = data['reqid']
    mech_id = data['mech_id'] 

    req = get_object_or_404( BookingRequest, id = req_id)
    mech = get_object_or_404( Mechanic, id = mech_id)
    req.assignedMechanic = mech
    req.requestState=1
    req.save()
    return JsonResponse({'result' : 'Mechanic Assigned'})