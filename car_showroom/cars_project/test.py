# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.management import call_command

from cars_project.models import Car, User
from cars_project.factories import UserFactory, CarFactory, DealerShipFactory

import vcr
import urllib2
from vcr.config import VCR

try:
    import simplejson as json
except ImportError:
    import json



class MyTestVCR(TestCase):

    def before_record_response(response):

        body = response['body']['string']
        response['body']['string'] = (body.replace(body, (json.dumps((json.loads(body)), indent=4, sort_keys=True)))).decode('utf-8')
        return response


    my_vcr = vcr.VCR(before_record_response=before_record_response)
    with my_vcr.use_cassette('fixtures/vcr_cassettes/synopsis24.json') as cass:
        response = urllib2.urlopen('http://127.0.0.1:9002/response_json/').read()
        assert len(cass) == 1
        assert cass.requests[0].uri == 'http://127.0.0.1:9002/response_json/'



class MyTest(TestCase):

    def test_denies_anonymous_user(self):
        response = self.client.get(reverse('index'), follow=True)
        self.assertRedirects(response, (('{}?next=/').format(reverse('login'))[1:]))
        response = self.client.post(reverse('index'), follow=True)
        self.assertRedirects(response, (('{}?next=/').format(reverse('login'))[1:]))

    def create_user_and_login(self):
        user = UserFactory.create(username='Uasya')
        user.set_password('123')
        user.save()
        login = self.client.login(username='Uasya', password='123')
        self.assertTrue(login)
        return user

    def test_belongs_to_car_dealer_dealership(self):
        self.create_user_and_login()
        cars = CarFactory.create_batch(3)
        user = User.objects.first()
        user.org = DealerShipFactory.create(cars=cars[:2])
        user.save()
        response = self.client.get(reverse('index'))
        self.assertEqual(list((response.context['car_list']).values_list('id', flat=True)),
                         list((Car.objects.filter(dealership=user.org)).values_list('id', flat=True)))

    def test_user_view_with_no_dealership(self):
        self.create_user_and_login()
        CarFactory.create_batch(3)
        response = self.client.get(reverse('index'))
        self.assertEqual(list((response.context['car_list'])), [])

    def test_car_get_car_logo_when_no_logo_should_return_default(self):
        CarFactory.create()
        car = Car.objects.get(id=1)
        self.assertEqual(car.get_car_logo(), "cars_project/car_logo/no-logo-available.gif" )

    def test_car_get_car_logo_when_logo_exist_should_return_car_logo(self):
        CarFactory.create(brand = 'Acura')
        car = Car.objects.get(id=1)
        car.save()
        self.assertEqual(car.get_car_logo(), "cars_project/car_logo/acura-logo.png")

    def test_car_get_car_logo_when_car_have_logo_should_return_it(self):
        CarFactory.create(car_logo = "cars_project/car_logo/just-blah-blah-blah.png")
        car = Car.objects.get(id=1)
        car.save()
        self.assertEqual(car.get_car_logo(), "cars_project/car_logo/just-blah-blah-blah.png")


class CommandsTestCase(TestCase):

    def test_sync_xml_cars(self):
        """ Test my sync_xml_cars command."""
        call_command('sync_xml_cars',
                     path='/home/moffio/car_showroom/car_showroom/cars_project/test_files/cars.xml')
        self.assertEqual(Car.objects.count(), 3)
