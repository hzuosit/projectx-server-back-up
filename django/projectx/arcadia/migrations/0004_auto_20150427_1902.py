# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arcadia', '0003_auto_20150420_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='co1info',
            options={'verbose_name_plural': 'CO1Info'},
        ),
        migrations.AlterModelOptions(
            name='customerinfo',
            options={'verbose_name_plural': 'CustomerInfo'},
        ),
        migrations.AlterModelOptions(
            name='huminfo',
            options={'verbose_name_plural': 'HumInfo'},
        ),
        migrations.AlterModelOptions(
            name='relationinfo',
            options={'verbose_name_plural': 'RelationInfo'},
        ),
        migrations.AlterModelOptions(
            name='tempinfo',
            options={'verbose_name_plural': 'TempInfo'},
        ),
        migrations.AlterField(
            model_name='co1info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 19, 2, 2, 59014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='huminfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 19, 2, 2, 58348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tempinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 19, 2, 2, 57645, tzinfo=utc)),
        ),
    ]
