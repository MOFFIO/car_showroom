# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from cars_project import views, form


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', form.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', form.LogoutView.as_view(), name='logout'),
    url(r'^register/$', form.RegisterFormView.as_view(), name='register'),
    url(r'^carform/$', views.CarCreate.as_view(), name='car_form'),
    url(r'^carform/(?P<car_id>\d+)/$', views.CarFormEdit.as_view(), name='car_form_edit'),
    url(r'^cars/(?P<car_id>\d+)/$', views.car_detail, name='car_detail'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



