# Generated by Django 3.2.6 on 2021-10-09 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211009_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='datetime',
            field=models.DateField(default=datetime.datetime(2021, 10, 9, 16, 34, 17, 890187)),
        ),
    ]
