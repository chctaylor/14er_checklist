from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Mountain

# Create your views here.

@login_required(login_url='/login')
def IndexView(request):
    return render(request, "main/index.html")

@login_required(login_url='/login')
def MountainsView(request):
    # Used to display database on html page
    data = Mountain.objects.all()

    mt = {
        "id": data
    }

    return render(request, "main/mountains.html", mt)