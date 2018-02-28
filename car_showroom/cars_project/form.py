# -*- coding: utf-8 -*-
from django import forms
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from cars_project.models import Car, CarAttributes
from cars_project.admin import MyUserCreationForm


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "cars_project/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterFormView(FormView):
    form_class = MyUserCreationForm
    success_url = "/login"
    template_name = "cars_project/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['uid', 'brand', 'price', 'car_logo', 'car_img', 'sold']


class CarFormAttributes(forms.ModelForm):
    class Meta:
        model = CarAttributes
        fields = ['paint', 'tires', 'trim']


class CarSold(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['sold']