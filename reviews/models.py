from django.db import models


class Review(models.Model):
    product_name = models.TextField()
    content = models.TextField()

    def __str__(self):
        return 'Review {} by {}'.format(self.product_name, self.content)
