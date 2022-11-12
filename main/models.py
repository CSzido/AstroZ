from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    img = models.ImageField(upload_to="images")
    f1 = models.CharField(max_length=100)
    f2 = models.CharField(max_length=100)
    f3 = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.IntegerField()
# Create your models here.
