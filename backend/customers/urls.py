from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup_view,
    home_view
    
)

app_name = 'customers'
urlpatterns = [
    path('login', login_view, name="login"),
    path('signup', signup_view, name="signup"),
    path('logout', logout_view, name="logout"),
    path('home', home_view, name="home"),
]
