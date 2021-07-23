from django import forms
from django.forms import ModelForm
from .models import Ascents, Mountain

class AscentsForm(ModelForm):
    class Meta:
        model = Ascents
        fields = '__all__'