from django.db import models

# Create your models here.
class Mountain(models.Model):
    mountain_name = models.CharField(max_length=200)
    mountain_height = models.PositiveSmallIntegerField(default=0)
    mountain_climbed = models.BooleanField(default=False)
    