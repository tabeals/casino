# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Deck(models.Model):
    image = models.ImageField(upload_to='deckOfCards/')
    suit = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    worth = models.IntegerField()



class Dice(models.Model):
    image = models.ImageField(upload_to='dieFace/')
    side = models.IntegerField()


class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description

class Customers(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    roomnum = models.IntegerField()
    len = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description





