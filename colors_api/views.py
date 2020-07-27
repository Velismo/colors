from django.db import models
from django.conf import settings


# Create your views here.

class GetColorsId(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    pantome_value = models.CharField(max_length=150)


class GetColors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=150)

