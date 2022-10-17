from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
bugun = timezone.now().astimezone()

def home(request):
    return render(request, "pages/home.html")

def RedirectTo(request, slug):
    redirect_to = get_object_or_404(URLshortner, slug=slug)

    return render(request, "pages/redirect.html", {"redirect_to": redirect_to})
