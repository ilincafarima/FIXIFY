from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from django.db import models
from authentication.models import CustomUser
from django.conf import settings

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()  # Changed from 'text' to 'body'
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
