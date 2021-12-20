from django.db import models
from django.contrib.auth.models import User
import datetime

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    author_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=50)
    content = models.TextField()
    creation_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)


class UpVote(models.Model):
    class Meta:
        unique_together = [
            ["post", "user"],
        ]

    post = models.ForeignKey(Post, related_name="upvotes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="upvotes", on_delete=models.CASCADE)
