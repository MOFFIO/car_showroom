# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-30 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_project', '0003_car_car_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_logo',
            field=models.ImageField(default='cars_project/car_logo/no-logo-available.gif', upload_to='cars_project/car_logo'),
        ),
    ]
