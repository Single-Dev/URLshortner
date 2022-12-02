from django.contrib.auth.views import LoginView , LogoutView
from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path('u/login/', LoginView.as_view(), name="login"),
    path('u/logout/', LogoutView.as_view(), name="logout"),
    path("<slug:slug>/", RedirectTo, name="redirect_to"),
    path("r/signup/", signup, name="signup")
]
