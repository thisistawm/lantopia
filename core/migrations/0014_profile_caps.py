# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20171020_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='caps',
            field=models.IntegerField(default=0),
        ),
    ]
