# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cars_project.models import Car

# Create your views here.

@login_required(login_url='login/')
def index(request):
    car_list = Car.cars_for_user(user=request.user)
    context = {'car_list': car_list}
    return render(request, 'cars_project/index.html', context)

@login_required(login_url='login/')
def car_detail(request, car_id):
    cars = Car.cars_for_user(user=request.user)
    context = {'car': cars.get(id=car_id)}
    return render(request, 'cars_project/car_detail.html', context)

