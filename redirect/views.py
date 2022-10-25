from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .form import *

def home(request):
    initial = {'key': 'value'}
    form = ShortnerFrom()
    if request.method == "POST":
        form = ShortnerFrom(request.POST)
        if form.is_valid():
            form.save()
            slug = form.cleaned_data.get('slug')
            messages.success(request, f'{slug}')
            return redirect('/')
    context={
        "form":form,
    }
    return render(request, "pages/home.html", context)

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'registration/signup.html', {"form":form})

def RedirectTo(request, slug):
    redirect_to = get_object_or_404(UrlShortner, slug=slug)

    return render(request, "pages/redirect.html", {"redirect_to": redirect_to})

