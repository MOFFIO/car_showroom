# -*- coding: utf-8 -*-
from django.conf.urls import url

from cars_project import views, form

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', form.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', form.LogoutView.as_view(), name='logout'),
    url(r'^register/$', form.RegisterFormView.as_view(), name='register'),
    url(r'^cars/(?P<car_id>\d+)/$', views.car_detail, name='car_detail'),
    ]
