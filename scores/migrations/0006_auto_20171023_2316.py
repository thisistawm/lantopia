# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 06:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0005_remove_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='user',
        ),
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]