from django.db import models


class Shop(models.Model):
    shop_title = models.CharField(max_length=500)
    shop_logo = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    distance = models.IntegerField(default=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.shop_title


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.product_title
