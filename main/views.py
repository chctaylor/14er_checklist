from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.

@login_required(login_url='/login')
def IndexView(request):

    return render(request, "main/index.html")

@login_required(login_url='/login')
def MountainsView(request):
    # Used to display database on html page
    mountains = Mountain.objects.all()

    return render(request, "main/mountains.html", {'mountains': mountains})

@login_required(login_url='/login')
def ClimberView(request, pk):
    climber = Climber.objects.get(id=pk)

    mountains = Mountain.objects.all()
    climbers = Climber.objects.all()

    ascents = climber.mountains.all()

    context = {'climber':climber, 'mountains':mountains, 'climbers':climbers, 'ascents':ascents}
    return render(request, "main/climber.html", context)