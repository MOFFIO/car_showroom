# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Car

# Create your views here.

@login_required(login_url='login/')
def index(request):
    if request.user.org:
        car_list = Car.objects.filter(dealership=request.user.org)
    else:
        car_list = []
    context = {'car_list': car_list}
    return render(request, 'cars_project/index.html', context)




