from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tags = TaggableManager()

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    #image = models.ImageField(upload_to='post', null=True)
    text = models.TextField()
    image = models.ImageField(upload_to='image', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    up_votes = models.ManyToManyField(User, blank=True, related_name='up_votes')
    down_votes = models.ManyToManyField(User, blank=True, related_name='down_votes')
    save_up = models.IntegerField()
    save_down = models.IntegerField()

    def __unicode__(self):
        return self.title

# def vote_save(self, *args, **kwargs):
#     super(Post, self).save(*args, **kwargs)
#     for post in Post.objects.exclude(pk=self.pk):
#         post.up_votes = self.up_votes
#         post.down_votes = self.down_votes
#         post.save_dupe()

def update_votes(sender, instance, **kwargs):
    up_count = instance.up_votes.all().count()
    down_count = instance.down_votes.all().count()

    print up_count
    print down_count

    instance.save_up = up_count
    instance.save_down = down_count

    instance.save()

m2m_changed.connect(update_votes, sender=Post.up_votes.through)


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    posted_on = models.ForeignKey('main.Post')
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.posted_on.title



