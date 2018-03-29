# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from cars_project.models import Car, RequestInfo
from cars_project.form import CarForm, CarFormAttributes, CarSold
from cars_project.utils import digit_from_list
from cars_project.decorators import render_to_template


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


@login_required(login_url='login/')
@render_to_template('cars_project/request_info.html')
def car_detail(request, car_id):
    cars = Car.cars_for_user(user=request.user)
    context = {'car': cars.get(id=car_id)}
    return context


@login_required(login_url='login/')
@render_to_template('cars_project/request_info.html')
def request_info(request, *args):
    if request.user.is_superuser:
        req_info = RequestInfo.objects.all()
        context = {'req_info': req_info}
        return context
    raise Http404('U are not SuperUser')


def response_json(request):
    car = Car.objects.get(id=8)
    return JsonResponse(Car.car_as_dict(car))


class CarListView(View):
    form_class = CarSold
    template_name = 'cars_project/index.html'

    @method_decorator(login_required(login_url='login/'))
    def get(self, request, *args, **kwargs):
        car_list = Car.cars_for_user(user=request.user)
        car_list = car_list.select_related('attributes')
        context = {'car_list': car_list}
        return render(request, self.template_name, context)

    @csrf_exempt
    @method_decorator(login_required(login_url='login/'))
    def post(self, request, *args, **kwargs):
        id_list = request.POST.get('id_list')
        upd = request.POST.get('update')
        if id_list:
            id_list = str(id_list)
            int_id_list = digit_from_list(id_list)
            car_list = (Car.objects.filter(id__in=int_id_list))
            if upd:
                car_list.update(sold=True)
            else:
                car_list.delete()
        return JsonResponse({})


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
            #import ipdb; ipdb.set_trace()
            return HttpResponseRedirect(reverse('car_detail', args=(car.id,)))
        context = {'car_form': car_form, 'car_form_attributes': car_form_attributes}
        return render(request, self.template_name, context)
