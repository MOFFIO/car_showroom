# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-20 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_project', '0010_requestinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinfo',
            name='url',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
