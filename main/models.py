from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tag = models.ManyToManyField('main.Tag', null=True)

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    text = models.TextField()
    tags = models.ManyToManyField('main.Tag')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    posted_on = models.ForeignKey('main.Post')

    def __unicode__(self):
        return self.posted_on.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField('main.Post', null=True)

    def __unicode__(self):
        return self.name
