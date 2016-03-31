# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arcadia', '0002_auto_20150420_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='co1info',
            name='device',
            field=models.ForeignKey(to='arcadia.RelationInfo', null=True),
        ),
        migrations.AlterField(
            model_name='co1info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 23, 52, 25, 303120, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='huminfo',
            name='device',
            field=models.ForeignKey(to='arcadia.RelationInfo', null=True),
        ),
        migrations.AlterField(
            model_name='huminfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 23, 52, 25, 302563, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='relationinfo',
            name='customer',
            field=models.ForeignKey(to='arcadia.CustomerInfo', null=True),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='device',
            field=models.ForeignKey(to='arcadia.RelationInfo', null=True),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 23, 52, 25, 301964, tzinfo=utc)),
        ),
    ]
