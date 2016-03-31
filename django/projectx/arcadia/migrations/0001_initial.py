# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CO1Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CO1', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customerID', models.EmailField(unique=True, max_length=254)),
                ('street', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.CharField(max_length=25, null=True, blank=True)),
                ('state', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HumInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('humidity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceID', models.IntegerField(unique=True)),
                ('customer', models.ForeignKey(to='arcadia.CustomerInfo')),
            ],
        ),
        migrations.CreateModel(
            name='TempInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.DecimalField(max_digits=5, decimal_places=2)),
                ('time', models.DateField(default=datetime.date.today)),
                ('device', models.ForeignKey(to='arcadia.RelationInfo')),
            ],
        ),
        migrations.AddField(
            model_name='huminfo',
            name='device',
            field=models.ForeignKey(to='arcadia.RelationInfo'),
        ),
        migrations.AddField(
            model_name='co1info',
            name='device',
            field=models.ForeignKey(to='arcadia.RelationInfo'),
        ),
    ]
