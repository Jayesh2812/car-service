from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name="mechanic_home"),
    path('login', views.login_view, name="login"),
    path('signup', views.signup_view, name="signup"),
    path('logout', views.logout_view, name="logout"),
    # path('', home_view, name="home"),
    path('create_bill/<int:reqid>',views.createBill,name="createbill"),
    path('requestcompleted/<int:reqid>',views.requestCompleted,name="requestcompleted"),
    path('assign', views.assign_mechanic)

]
