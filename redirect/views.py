from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .form import *
from django.utils import timezone

def home(request):
    form = ShortnerFrom()
    if request.method == "POST":
        form = ShortnerFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        "form":form
    }
    return render(request, "pages/home.html", context)

def RedirectTo(request, slug):
    # detect = URLshortner.objects.filter(date__date=timezone.now()).all()

    redirect_to = get_object_or_404(URLshortner, slug=slug)

    return render(request, "pages/redirect.html", {"redirect_to": redirect_to})

