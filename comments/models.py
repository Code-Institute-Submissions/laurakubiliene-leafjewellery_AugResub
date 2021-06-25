from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return 'Comment {} by {}'.format(self.name, self.email, self.content)
