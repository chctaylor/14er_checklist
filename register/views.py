from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from main.models import *

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()

            Climber.objects.create(
                user = user,
                climber_name = user.first_name,
            )

        return redirect("/login") # need to define path
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form":form})
