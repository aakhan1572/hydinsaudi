# Generated by Django 4.1.7 on 2023-05-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expads", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expatad",
            name="cover_photo",
            field=models.FileField(
                blank=True, null=True, upload_to="users/cover_photos"
            ),
        ),
    ]
