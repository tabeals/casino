# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Deck
from .models import Dice
from .models import Employee
from .models import Customers

# Register your models here.
admin.site.register(Deck)
admin.site.register(Dice)
admin.site.register(Employee)
admin.site.register(Customers)

