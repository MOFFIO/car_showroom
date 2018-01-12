# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Car, CarAttributes, Dealership
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from django.template import Context, loader

# Create your views here.

@login_required(login_url='login/')
def index(request):
    car_list = Car.objects.all()
    context = {'car_list': car_list}
    return render(request, 'cars_project/index.html', context)




