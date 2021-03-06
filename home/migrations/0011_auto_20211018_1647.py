# Generated by Django 3.2.6 on 2021-10-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211018_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='servers',
            name='server_type',
            field=models.CharField(choices=[('CUCM', 'Cucm'), ('CUC', 'Cuc'), ('UCS', 'Ucs'), ('UCCX', 'Uccx')], max_length=100),
        ),
        migrations.AlterField(
            model_name='servers',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
