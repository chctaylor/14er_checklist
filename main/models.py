from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Mountain(models.Model):
    mountain_name = models.CharField(max_length=200, null=True)
    mountain_height = models.PositiveSmallIntegerField(default=0)
    mountain_range = models.CharField(max_length=50, null=True)
    climbers = models.ManyToManyField('Climber', through='Ascents')

    def __str__(self):
        return self.mountain_name

class Climber(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    climber_name = models.CharField(max_length=200, null=True)
    mountains = models.ManyToManyField(Mountain, through='Ascents')

    def __str__(self):
        return self.climber_name

class Ascents(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    climber = models.ForeignKey(Climber, on_delete=models.CASCADE)

    def __str__(self):
        return self.climber.climber_name