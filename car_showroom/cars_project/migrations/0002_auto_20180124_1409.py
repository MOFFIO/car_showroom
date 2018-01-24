# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-24 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
