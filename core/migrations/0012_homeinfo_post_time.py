# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_homeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinfo',
            name='post_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
