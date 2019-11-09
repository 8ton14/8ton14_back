from django.db import models
# from ..recommend.models import *

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(default="")
    tags = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title


class Comment(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    content = models.TextField(default="")
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:50]