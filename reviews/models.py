from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Review(models.Model):
    product_name = models.TextField()
    content = models.TextField()

    def __str__(self):
        return 'Review {} by {}'.format(self.content)