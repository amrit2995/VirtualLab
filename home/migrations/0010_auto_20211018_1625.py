# Generated by Django 3.2.6 on 2021-10-18 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_auto_20211012_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('server_type', models.CharField(max_length=20)),
                ('hostname', models.CharField(default=None, max_length=20, unique=True)),
                ('ipaddress', models.GenericIPAddressField(default=None, primary_key=True, serialize=False)),
                ('fqdn', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='cucm',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='uccx',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='ucs',
            name='creator',
        ),
        migrations.DeleteModel(
            name='CUC',
        ),
        migrations.DeleteModel(
            name='CUCM',
        ),
        migrations.DeleteModel(
            name='UCCX',
        ),
        migrations.DeleteModel(
            name='UCS',
        ),
    ]