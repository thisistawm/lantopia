# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_auto_20171023_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]