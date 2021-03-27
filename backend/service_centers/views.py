from django.shortcuts import render
from customers.models import *
from service_centers.models import *
from mechanics.models import *
from django.db.models import Q
# Create your views here.
def home(request):
    serviceCenterObj=ServiceCenter.objects.get(id=1)
    requestObjs=BookingRequest.objects.filter(requestedTo=serviceCenterObj)
    activeRequests=requestObjs.filter(requestState=0)
    inactiveRequests=requestObjs.filter(~Q(requestState=0))
    mechanics=Mechanic.objects.filter(serviceCenter=serviceCenterObj)
    print(activeRequests)
    context={
        'activerequests':activeRequests,
        'pastrequests':inactiveRequests,
        'mechanics':mechanics
    }
    return render(request,'service_centers/home.html',context)