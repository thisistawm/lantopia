# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_profile_unpacked'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=200)),
                ('details', models.TextField(blank=True, max_length=1000)),
                ('nextUp', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
