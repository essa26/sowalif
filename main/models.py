from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    text = models.TextField()
    tags = models.ManyToManyField('main.Tag', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    posted_on = models.ForeignKey('main.Post')
    date_created = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.posted_on.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    #post = models.ManyToManyField('main.Post')
    #posts = models.ManyToManyField('main.Post')

    def __unicode__(self):
        return self.name
