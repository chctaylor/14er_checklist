from django.forms import ModelForm
from .models import Ascents

class AscentsForm(ModelForm):
    class Meta:
        model = Ascents
        fields = ['climber', 'mountain']