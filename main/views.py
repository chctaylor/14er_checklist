from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseForbidden
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
def MtView(request, pk):
    mountain = Mountain.objects.get(mountain_name=pk)

    context = {'mountain':mountain}
    return render(request, "main/mt.html", context)


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

    AscentFormSet = inlineformset_factory(Climber, Ascents, fields=('mountain',), extra=5, can_delete_extra=False)
    formset = AscentFormSet(queryset=Ascents.objects.none(), instance=climber)

    if request.method == 'POST':
        formset = AscentFormSet(request.POST, instance=climber)
        if formset.is_valid():
            formset.save()
            return redirect('main:climber', pk)

    context = {'formset':formset, 'climber':climber}
    
    if not climber.user == request.user:
        return HttpResponseForbidden("Access Denied: Cannot add ascents for other users")
    else:
        return render(request, "main/ascents_form.html", context)