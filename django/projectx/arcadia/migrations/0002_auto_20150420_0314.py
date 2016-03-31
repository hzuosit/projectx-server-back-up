# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arcadia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='co1info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 3, 14, 58, 172489, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='huminfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 3, 14, 58, 171849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 3, 14, 58, 171211, tzinfo=utc)),
        ),
    ]
