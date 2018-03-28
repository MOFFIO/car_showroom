# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class CarsProjectConfig(AppConfig):
    name = 'cars_project'

    def ready(self):
        import cars_project.signals