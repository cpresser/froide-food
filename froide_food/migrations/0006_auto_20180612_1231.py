# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('froide_food', '0005_auto_20180607_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuerequest',
            name='last_request',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venuerequest',
            name='last_status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
