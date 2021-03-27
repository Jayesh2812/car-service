from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
# from mechanics.models import BookingRequest
# Create your models here.

#Mechanic Model
class ServiceCenter(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNo=models.DecimalField(max_digits=10,decimal_places=0)
    centerName=models.CharField(max_length=300)
    openingTime=models.TimeField()
    closingTime=models.TimeField()
    locationState=models.CharField(max_length=200)
    locationCity=models.CharField(max_length=200)
    locationPinCode=models.DecimalField(max_digits=6,decimal_places=0)
    address=models.CharField(max_length=500)
    numberOfMechs=models.DecimalField(max_digits=4,decimal_places=0)
    baseVisitingCharges=models.DecimalField(max_digits=8,decimal_places=2)
    availableServices= models.CharField(max_length=800)         #along with type of service

    def __str__(self):
        return self.centerName

#Bills
