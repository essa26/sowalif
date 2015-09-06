# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 6, 10, 36, 7, 428048, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=1, auto_now=True),
            preserve_default=False,
        ),
    ]
