# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='down_votes',
            field=models.ManyToManyField(related_name='down_votes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='up_votes',
            field=models.ManyToManyField(related_name='up_votes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
