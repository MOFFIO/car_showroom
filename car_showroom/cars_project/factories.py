# -*- coding: utf-8 -*-
import factory

from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from cars_project.models import Car, CarAttributes, Dealership


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'boris%s' % n)
    password = '1234567890'
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)

class CarAttributesFactory(DjangoModelFactory):
    class Meta:
        model = CarAttributes

    paint = 'red'
    tires = 'regular'
    trim = 'regular'

class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    uid = factory.Sequence(lambda g: '%s' % g)
    brand = 'JEEP'
    attributes = factory.SubFactory(CarAttributesFactory)

class DealerShipFactory(DjangoModelFactory):
    class Meta:
        model = Dealership

    @factory.post_generation
    def cars(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of groups were passed in, use them
            for car in extracted:
                self.cars.add(car)

