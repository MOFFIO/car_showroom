# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

Indicate Celery to use the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars_project.settings')
app = Celery(broker="amqp://myuser:mypassword@localhost:5672/myvhost")
# This line will tell Celery to autodiscover all your tasks.py that are in your app folders
app.config_from_object('django.conf:settings')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#app.conf.update(
#    CELERY_DEFAULT_QUEUE = "cars_project",
#    CELERY_DEFAULT_EXCHANGE = "cars_project",
#    CELERY_DEFAULT_EXCHANGE_TYPE = "direct",
#    CELERY_DEFAULT_ROUTING_KEY = "cars_project",
#)