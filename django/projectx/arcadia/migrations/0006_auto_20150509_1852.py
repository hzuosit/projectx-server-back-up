# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arcadia', '0005_auto_20150430_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempinfo',
            name='user',
            field=models.ForeignKey(to='arcadia.DeviceBook', null=True),
        ),
        migrations.AlterField(
            model_name='co1info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 9, 22, 52, 4, 271018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='huminfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 9, 22, 52, 4, 270487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 9, 22, 52, 4, 271617, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 9, 22, 52, 4, 269849, tzinfo=utc)),
        ),
    ]
