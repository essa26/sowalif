# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField()),
<<<<<<< HEAD
=======
<<<<<<< HEAD
                ('date_created', models.DateTimeField(auto_now=True)),
=======
>>>>>>> 9dd0c31aa7e2218d9f2710e054dd809e501b0052
>>>>>>> f887e4e7bbddec2b5b4a0711ef7082530a598895
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
<<<<<<< HEAD
=======
<<<<<<< HEAD
                ('date_created', models.DateTimeField(auto_now=True)),
=======
>>>>>>> 9dd0c31aa7e2218d9f2710e054dd809e501b0052
>>>>>>> f887e4e7bbddec2b5b4a0711ef7082530a598895
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
<<<<<<< HEAD
                ('posts', models.ManyToManyField(to='main.Post')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ManyToManyField(to='main.Tag')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
=======
<<<<<<< HEAD
=======
                ('posts', models.ManyToManyField(to='main.Post')),
>>>>>>> 9dd0c31aa7e2218d9f2710e054dd809e501b0052
>>>>>>> f887e4e7bbddec2b5b4a0711ef7082530a598895
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='main.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_on',
            field=models.ForeignKey(to='main.Post'),
        ),
    ]
