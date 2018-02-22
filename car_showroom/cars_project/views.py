# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.utils.decorators import method_decorator

from cars_project.models import Car, RequestInfo
from cars_project.form import CarForm, CarFormAttributes


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
def request_info(request):
    if request.user.is_superuser:
        req_info = RequestInfo.objects.all()
        context = {'req_info': req_info}
        return render(request, 'cars_project/request_info.html', context)
    raise Http404('U are not SuperUser')


class CarFormEdit(View):
    form_class = CarForm
    form_attibutes_class = CarFormAttributes
    template_name = 'cars_project/car_form.html'

    @method_decorator(login_required(login_url='login/'))
    def get(self, request, car_id, *args, **kwargs):
        carr = Car.objects.get(id=car_id)
        car_form = self.form_class(instance=carr)
        car_form_attributes = self.form_attibutes_class(instance=carr.attributes)
        context = {'car_form': car_form, 'car_form_attributes': car_form_attributes}
        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url='login/'))
    def post(self, request, car_id, *args, **kwargs):
        carr = Car.objects.get(id=car_id)
        car_form = self.form_class(request.POST, request.FILES, instance=carr)
        car_form_attributes = self.form_attibutes_class(request.POST, instance=carr.attributes)
        if car_form.is_valid() and car_form_attributes.is_valid():
            car_attributes = car_form_attributes.save()
            car = car_form.save(commit=False)
            car.attributes = car_attributes
            car.save()
            car.dealership_set.add(request.user.org)
            return HttpResponseRedirect(reverse('car_detail', args=(car.id,)))
        context = {'car_form': car_form, 'car_form_attributes': car_form_attributes}
        return render(request, self.template_name, context)


class CarCreate(View):
    form_class = CarForm
    form_attibutes_class = CarFormAttributes
    template_name = 'cars_project/car_form.html'

    @method_decorator(login_required(login_url='login/'))
    def get(self, request, *args, **kwargs):
        car_form = self.form_class(request.GET)
        car_form_attributes = self.form_attibutes_class(request.GET)
        context = {'car_form': car_form, 'car_form_attributes': car_form_attributes}
        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url='login/'))
    def post(self, request, *args, **kwargs):
        car_form = self.form_class(request.POST)
        car_form_attributes = self.form_attibutes_class(request.POST, request.FILES)
        if car_form.is_valid() and car_form_attributes.is_valid():
            car_attributes = car_form_attributes.save()
            car = car_form.save(commit=False)
            car.attributes = car_attributes
            car.save()
            car.dealership_set.add(request.user.org)
            return HttpResponseRedirect(reverse('car_detail', args=(car.id,)))
        context = {'car_form': car_form, 'car_form_attributes': car_form_attributes}
        return render(request, self.template_name, context)
