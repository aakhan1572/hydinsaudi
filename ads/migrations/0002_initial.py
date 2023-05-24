# Generated by Django 4.1.7 on 2023-05-21 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EVChargingLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("station_name", models.CharField(max_length=250)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]
