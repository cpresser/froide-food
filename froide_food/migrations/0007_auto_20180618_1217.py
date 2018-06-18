# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 10:17
from __future__ import unicode_literals

from django.db import migrations


def store_last_status(apps, schema_editor):
    VenueRequest = apps.get_model('froide_food', 'VenueRequest')
    VenueRequestItem = apps.get_model('froide_food', 'VenueRequestItem')

    for venue in VenueRequest.objects.all():
        vris = VenueRequestItem.objects.filter(venue=venue).order_by('-timestamp')
        if vris:
            vri = vris[0]
            venue.last_request = vri.timestamp
            if vri.foirequest:
                venue.last_status = vri.foirequest.status
            venue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('froide_food', '0006_auto_20180612_1231'),
    ]

    operations = [
        migrations.RunPython(store_last_status),
    ]
