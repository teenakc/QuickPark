# Generated by Django 4.1.7 on 2023-11-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingapp', '0002_parkingarea_userreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
