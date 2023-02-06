from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    ELECTRONICS = 'EL'
    CLOTHING = 'CL'
    HOMEACCESSORIES = 'HA'
    HEALTH = 'HE'
    BEAUTY = 'BE'
    CATEGORIES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (HOMEACCESSORIES, 'HomeAccessories'),
        (HEALTH, 'Health'),
        (BEAUTY, 'Beauty'),
    ]
    name = models.CharField(max_length=100, blank=False,
                            null=False, verbose_name="Name")
    category = models.CharField(max_length=2,
                                choices=CATEGORIES,
                                default=ELECTRONICS, verbose_name="Category")
    brand = models.CharField(max_length=50, verbose_name="Brand")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=20, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.client + " - " + self.product
