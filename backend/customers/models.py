from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#customer model
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNo=models.DecimalField(max_digits=10,decimal_places=0)
    emailId=models.EmailField()



