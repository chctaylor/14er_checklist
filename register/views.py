from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return HttpResponse("Registered") # need to define path
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form":form})
