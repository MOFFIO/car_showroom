# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

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
