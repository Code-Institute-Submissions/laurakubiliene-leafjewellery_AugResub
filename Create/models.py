from django.db import models
from . import Create

# Create your models here.


class Options(models.Model):
    # options to choose from
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ManyToManyField('products', through='products')

    def __str__(self):
        return self.name


class Product(models.Model): 
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    options = models.ManyToManyField(Options)

    def __str__(self):
        return self.name

