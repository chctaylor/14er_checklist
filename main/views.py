from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AscentsForm
from .models import *

# Create your views here.

@login_required(login_url='/login')
def IndexView(request):

    return render(request, "main/index.html")

@login_required(login_url='/login')
def MountainsView(request):
    
    climbers = Climber.objects.all()
    # Used to display database on html page
    mountains = Mountain.objects.all()

    context = {'mountains':mountains, 'climbers':climbers}
    return render(request, "main/mountains.html", context)

@login_required(login_url='/login')
def ClimberView(request, pk):
    climber = Climber.objects.get(id=pk)
    mountains = Mountain.objects.all()
    climbers = Climber.objects.all()
    ascents = climber.mountains.all()

    context = {'climber':climber, 'mountains':mountains, 'climbers':climbers, 'ascents':ascents}
    return render(request, "main/climber.html", context)

@login_required(login_url='/login')
def addAscentsView(request, pk):
    climber = Climber.objects.get(id=pk)

    form = AscentsForm(initial={'climber':climber})
    if request.method == 'POST':
        form = AscentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:climber', pk)

    context = {'form':form, 'climber':climber}
    return render(request, "main/ascents_form.html", context)