# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150910_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',

            field=models.ImageField(null=True, upload_to=b'image', blank=True),
        ),
    ]
