from django.conf.urls import url

from cars_project import views

urlpatterns = [
    url(r'^', views.index, name='index')
    ]
