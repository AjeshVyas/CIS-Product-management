from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length = 50)
    thumbnail = models.ImageField(upload_to='product_images', default='product_images/default.jpg')
    tags = models.CharField(max_length=100)
    description = models.CharField(max_length = 5000)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)