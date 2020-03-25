# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOISES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length =100)
    submitter = models.CharField(max_length =100)
    species = models.CharField(max_length =100)
    breed = models.CharField(max_length =30, blank=True)
    description = models.TextField()
    sex = models.CharField(choises=SEX_CHOISES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField(null=True)


