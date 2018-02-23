# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'print all models'


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print apps.get_models()
