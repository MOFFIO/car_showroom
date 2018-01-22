# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from cars_project.models import Car, CarAttributes, Dealership, User



admin_register = admin.site.register
admin_register(Car)
admin_register(CarAttributes)
admin_register(Dealership)
admin_register(User)


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username']
