from django.shortcuts import render,redirect
from customers.models import *
from service_centers.models import *
from mechanics.models import *
from django.db.models import Q
from datetime import datetime
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