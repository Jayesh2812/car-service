from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Mechanic)
admin.site.register(BookingRequest)
admin.site.register(BillGenerated)