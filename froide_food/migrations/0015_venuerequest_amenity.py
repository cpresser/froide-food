# Generated by Django 2.2.4 on 2019-10-02 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_amenities", "0001_initial"),
        ("froide_food", "0014_foodauthoritystatus"),
    ]

    operations = [
        migrations.AddField(
            model_name="venuerequest",
            name="amenity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="django_amenities.Amenity",
            ),
        ),
    ]
