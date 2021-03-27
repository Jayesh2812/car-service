from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name="mechanic_home"),
    path('create_bill/<int:reqid>',views.createBill,name="createbill"),
    path('requestcompleted/<int:reqid>',views.requestCompleted,name="requestcompleted"),
]
