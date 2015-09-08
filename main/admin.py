from django.contrib import admin
from main.models import UserProfile, Post, Comment, Tag

from main.models import Post, Comment, Tag
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)