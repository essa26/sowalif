from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, required=True)
    tag = models.ManyToManyField('main.Tag')

    def __unicode__(self):
        return self.user.username
