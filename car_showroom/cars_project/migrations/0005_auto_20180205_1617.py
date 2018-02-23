# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-05 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_project', '0004_car_car_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_img',
            field=models.ImageField(default='static/cars_project/car_foto/no_img.png', upload_to='cars_project/car_foto'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_logo',
            field=models.ImageField(default='static/cars_project/car_logo/no-logo-available.gif', upload_to='cars_project/car_logo'),
        ),
    ]