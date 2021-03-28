
from django.urls import path
from .views import signup_view,home, details_view, login_view, logout_view

app_name = 'service_center'
urlpatterns = [
    path('',home,name="home"),
    path('signup',signup_view,name="signup"),
    path('details',details_view,name="details"),
    path('login',login_view,name="login"),
    path('logout',login_view,name="logout"),
]
