from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    img = models.CharField(max_length=7000)
    f1 = models.CharField(max_length=100)
    f2 = models.CharField(max_length=100)
    f3 = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.IntegerField()


class Order(models.Model):
    name = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=1000)
    Email = models.EmailField()

    def __str__(self):
        return self.name
# Create your models here.
