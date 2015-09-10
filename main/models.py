from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tags = TaggableManager()

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    up_votes = models.ManyToManyField(User, blank=True, related_name='up_votes')
    down_votes = models.ManyToManyField(User, blank=True, related_name='down_votes')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    posted_on = models.ForeignKey('main.Post')
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.posted_on.title



