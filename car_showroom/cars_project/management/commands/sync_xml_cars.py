# -*- coding: utf-8 -*-
import os

from lxml import etree
from django.core.management.base import BaseCommand, CommandError

from cars_project.models import Car, CarAttributes



class Command(BaseCommand):
    help = 'Add car from *.xml db file'


    def add_arguments(self, parser):
        parser.add_argument('path', default='/home/moffio/my_python/cars.xml', nargs='*')

    def handle(self, *args, **options):
        if not os.path.isfile(options['path']):
            raise CommandError('Wrong path, try again')

        tree = etree.parse(options['path'])
        rawss = tree.findall('vehicle')
        all_cars = []
        for idd, raw in enumerate(rawss, start=1):
            car = [
                idd,
                raw.get('make'),
                int(raw.xpath('price')[0].text),
                raw.xpath('color')[0].text,
                raw.xpath('tires')[0].text,
                'Regular'
            ]
            all_cars.append(car)
        self.add_cars(all_cars)

    def add_cars(self, all_cars):
        for item in all_cars:
            car_attr = CarAttributes(paint=item[3], tires=item[4], trim=item[5])
            car_attr.save()
            carr = Car(uid=item[0], brand=item[1], price=item[2], attributes=car_attr)
            carr.save()

