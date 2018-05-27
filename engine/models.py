from django.db import models
from django.db.models import F
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    img = models.CharField(max_length=200, default="/static/media/no-image.jpg")
    price = models.IntegerField(default=0, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

