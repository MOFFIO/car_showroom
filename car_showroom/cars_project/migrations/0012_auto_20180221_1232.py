# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-21 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_project', '0011_requestinfo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars_project.Dealership'),
        ),
    ]
