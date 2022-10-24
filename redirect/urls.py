from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("<slug:slug>", RedirectTo, name="redirect_to_slash"),
    path("<slug:slug>/", RedirectTo, name="redirect_to")
]
