# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Car, CarAttributes, Dealership, User

admin_register = admin.site.register
admin_register(Car)
admin_register(CarAttributes)
admin_register(Dealership)
admin_register(User)