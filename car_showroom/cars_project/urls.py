from django.conf.urls import url

from cars_project import views
from cars_project import form

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', form.LoginFormView.as_view()),
    url(r'^logout/$', form.LogoutView.as_view())
    ]
