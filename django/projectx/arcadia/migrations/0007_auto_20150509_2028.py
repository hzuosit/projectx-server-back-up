# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arcadia', '0006_auto_20150509_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='moinfo',
            name='user',
            field=models.ForeignKey(to='arcadia.DeviceBook', null=True),
        ),
        migrations.AlterField(
            model_name='co1info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 0, 28, 4, 677142, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='huminfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 0, 28, 4, 676613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 0, 28, 4, 677691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 0, 28, 4, 675953, tzinfo=utc)),
        ),
    ]
