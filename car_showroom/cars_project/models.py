# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser




class Car(models.Model):

    uid = models.CharField(max_length=30, blank=True)
    brand = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    attributes = models.OneToOneField('CarAttributes')

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

class Dealership(models.Model):
    cars = models.ManyToManyField(Car)

class User(AbstractUser):
    org = models.ForeignKey(Dealership, null=True)



