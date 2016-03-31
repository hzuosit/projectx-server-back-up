# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arcadia', '0004_auto_20150427_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=False)),
                ('value', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'DeviceBook',
            },
        ),
        migrations.CreateModel(
            name='MoInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motion', models.BooleanField(default=False)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 4, 30, 19, 29, 19, 270357, tzinfo=utc))),
                ('device', models.ForeignKey(to='arcadia.RelationInfo', null=True)),
            ],
            options={
                'verbose_name_plural': 'MotionInfo',
            },
        ),
        migrations.AlterField(
            model_name='co1info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 19, 29, 19, 269754, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='huminfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 19, 29, 19, 269202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 19, 29, 19, 268579, tzinfo=utc)),
        ),
    ]
