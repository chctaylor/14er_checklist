from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Mountain(models.Model):
    mountain_name = models.CharField(max_length=200)
    mountain_height = models.PositiveSmallIntegerField(default=0)
    mountain_climbed = models.BooleanField(default=False)
    mountain_range = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.mountain_name