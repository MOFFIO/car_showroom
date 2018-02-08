# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.views.generic.base import View
#from django.views.generic.edit import FormView

from cars_project.models import Car
from cars_project.form import CarForm, CarFormAttributes




#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy


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

@login_required(login_url='login/')
def carform(request):
    car_form = CarForm(request.POST)
    car_form_attributes = CarFormAttributes(request.POST)
    if car_form.is_valid() and car_form_attributes.is_valid():
        car_attributes = car_form_attributes.save()
        car = car_form.save(commit = False)
        car.attributes = car_attributes
        car.save()
        car.dealership_set.add(request.user.org)
    context = {'car_form': car_form, 'car_form_attributes': car_form_attributes}
    return render(request, 'cars_project/car_form.html', context)




















#class CarCreate(CreateView):
    #template_name = 'cars_project/car_form.html'
    #model = Car
    #fields = ['uid', 'brand', 'price', 'attributes', 'car_logo', 'car_img', 'sold']
#
    #@login_required(login_url='login/')
    #def form_valid(self, form):
        #form.instance.created_by = self.request.user
        #return super(CarCreate, self).form_valid(form)
#
#class CarUpdate(UpdateView):
    #model = Car
    #fields = ['uid', 'brand', 'price', 'attributes', 'car_logo', 'car_img', 'sold']
#
#class CarDelete(DeleteView):
    #model = Car
    #success_url = reverse_lazy('car_detail')








#class CarFormView(CreateView):
    #template_name = 'cars_project/carform.html'
    #model = Car
    #fields = ['brand', 'price', 'paint', 'tires', 'trim']
    #success_url = '/'
    #@login_required(login_url='login/')
    #def form_valid(self, form):
        #return super(CarFormView, self).form_valid(form)


    #modell = CarAttributes
    #fieldss = ['paint', 'tires', 'trim']
