# -*- coding: utf-8 -*-
from django.conf.urls import url

from cars_project import views, form
#from cars_project.views import CarCreate, CarUpdate, CarDelete

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', form.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', form.LogoutView.as_view(), name='logout'),
    url(r'^register/$', form.RegisterFormView.as_view(), name='register'),
    url(r'carform/$', views.carform, name='car_form'),
    url(r'^cars/(?P<car_id>\d+)/$', views.car_detail, name='car_detail'),
    ]










    #url(r'carform/(?P<pk>[0-9]+)/$', CarUpdate.as_view(), name='car_update'),
    #url(r'carform/(?P<pk>[0-9]+)/delete/$', CarDelete.as_view(), name='car_delete'),