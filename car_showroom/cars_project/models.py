# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import fnmatch

#from urlparse import urlparse
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.staticfiles.templatetags.staticfiles import static
#from sorl.thumbnail import get_thumbnail
from django.urls import reverse


class Car(models.Model):

    uid = models.CharField(max_length=30, blank=True)
    brand = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    attributes = models.OneToOneField('CarAttributes')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    sold = models.BooleanField(default=False)
    car_img = models.ImageField(upload_to="cars_project/car_foto", default="cars_project/car_foto/no_img.png")
    car_logo = models.ImageField(upload_to="cars_project/car_logo", default="cars_project/car_logo/no-logo-available.gif")

    def __unicode__(self):
        return '<Car_uid: %s, Brand: %s>' % (self.uid, self.brand)

    def car_as_dict(self):
        car = {
            'uid' : self.uid,
            'brand' : self.brand,
            'price' : self.price,
            'paint' : self.attributes.paint,
            'tires' : self.attributes.tires,
            'trim' : self.attributes.trim
            }
        return car

    @classmethod
    def cars_for_user(cls, user):
        if user.org:
            return Car.objects.filter(dealership=user.org)
        return Car.objects.none()

    def get_car_logo(self):
        if not self.car_logo or self.car_logo == 'cars_project/car_logo/no-logo-available.gif':
            dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
            logo_path = "/media/cars_project/car_logo/"
            car_logo_path = os.path.join(dirname + logo_path)
            for item in os.listdir(car_logo_path):
                if fnmatch.fnmatch(item, (self.brand.lower() + '*.*')):
                    self.car_logo = os.path.join("cars_project/car_logo", item)
                    self.save()
        return self.car_logo

    def get_image_483x321(self):
        #import ipdb; ipdb.set_trace()
        #url = self.car_img.url
        return self.car_img
        #return get_thumbnail(url, '483x321', crop='center', quality=99)

    def get_absolute_url(self):
        return reverse('car_form', kwargs={'car_id': self.id})


class CarAttributes(models.Model):

    REGULAR = 'RG'
    RAIN = 'RN'
    SPORT = 'ST'
    SNOW = 'SW'
    CAR_ATTRIBUTES = (
        (REGULAR, 'Regular'),
        (RAIN, 'Rain'),
        (SPORT, 'Sport'),
        (SNOW, 'Snow')
    )
    paint = models.CharField(max_length=30,)
    tires = models.CharField(max_length=30,
                             choices=CAR_ATTRIBUTES,
                             default=REGULAR)
    trim = models.CharField(max_length=30,
                            default='Regular')

    def get_paint_text(self):
        return self.paint.lower()


class Dealership(models.Model):

    cars = models.ManyToManyField(Car)
    logo = models.ImageField(upload_to="cars_project/logo", default="cars_project/car_logo/no-logo-available.gif")


class User(AbstractUser):

    org = models.ForeignKey(Dealership, null=True, blank=True)


class RequestInfo(models.Model):

    user = models.ForeignKey(User, null=True)
    time = models.DateTimeField(auto_now=True)
    post_data = models.TextField() # request.POST
    http_cookie = models.TextField()
    url = models.URLField(max_length=255, null=True)
