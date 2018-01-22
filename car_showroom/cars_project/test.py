# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.management import call_command

from cars_project.models import Car, User
from cars_project.factories import UserFactory, CarFactory, DealerShipFactory

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


class CommandsTestCase(TestCase):

    def test_sync_xml_cars(self):
        """ Test my sync_xml_cars command."""
        call_command('sync_xml_cars',
                     path='/home/moffio/car_showroom/car_showroom/cars_project/test_files/cars.xml')
        self.assertEqual(Car.objects.count(), 3)
