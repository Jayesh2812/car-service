from django.db import models
from service_centers.models import ServiceCenter
from django.contrib.auth.models import User
from customers.models import Customer
# Create your models here.

#Mechanic Model
class Mechanic(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    serviceCenter=models.ForeignKey(ServiceCenter,on_delete=models.CASCADE)
    phoneNo=models.DecimalField(max_digits=10,decimal_places=0)
    emailId=models.EmailField()

    
    def __str__(self):
        return self.user.username


requestStates=[
    (0,'pending'),
    (1,'accepted'),
    (2,'rejected'),
    (3,'completed')
]

vehicleTypes=[
    (0,'two wheeler'),
    (1,'three wheeler'),
    (2,'four wheeler'),
    (3,'heavy vehicle'),
]

class BookingRequest(models.Model):
    requestedBy=models.ForeignKey(Customer,on_delete=models.CASCADE)
    requestedTo=models.ForeignKey(ServiceCenter,on_delete=models.CASCADE)
    assignedMechanic=models.ForeignKey(Mechanic,on_delete=models.CASCADE,blank=True,null=True)
    vehicleNumber=models.DecimalField(max_digits=6,decimal_places=0)
    vehicleType=models.IntegerField(choices=vehicleTypes)
    requestState=models.IntegerField(choices=requestStates)
    problemDescriptionByCustomer=models.CharField(max_length=500)
    problemDescriptionByMech=models.CharField(max_length=500,blank=True,null=True)
    mechanicArrived=models.BooleanField(default=False)  #customer has to marked as arrived
    bill=models.DecimalField(max_digits=8,decimal_places=2,default=0)

    # time
    requestedTime=models.DateTimeField()
    requestAcceptanceTime=models.DateTimeField(blank=True,null=True)
    mechanicArrivalTime=models.DateTimeField(blank=True,null=True)
    serviceCompleteTime=models.DateTimeField(blank=True,null=True)
    
    #location
    locationState=models.CharField(max_length=500)
    locationCity=models.CharField(max_length=500)
    locationPinCode=models.DecimalField(max_digits=6,decimal_places=0)
    address=models.CharField(max_length=500)# this will be added from gmap api

    
    

class BillGenerated(models.Model):
    associatedRequest=models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    problemResolved=models.CharField(max_length=300)
    cost=models.DecimalField(max_digits=5,decimal_places=2)