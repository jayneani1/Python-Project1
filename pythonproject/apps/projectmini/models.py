from django.db import models
from django.utils import timezone

class InstaPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
