# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150905_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(to='main.Post', null=True),
        ),
    ]
