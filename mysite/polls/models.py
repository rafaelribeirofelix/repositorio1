from datetime import date
from tokenize import Name
from django.db import models
from django import forms


class Webpage(models.Model):
    name = models.CharField(max_length=264, unique= True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


# Create your models here.
