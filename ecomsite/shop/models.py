from django.db import models


# Create your models here.
class Product(models.Model):
    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    catagory = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)  # Should host on other website


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
