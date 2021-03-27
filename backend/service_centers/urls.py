
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="service_home")
]
