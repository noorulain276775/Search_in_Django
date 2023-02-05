from django.db import models


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
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Name")
    category = models.CharField(max_length=2,
                                choices=CATEGORIES,
                                default=ELECTRONICS, verbose_name="Category")
    brand = models.CharField(max_length=50, verbose_name="Brand")
    price = models.DecimalField(verbose_name="Price")
    quantity = models.IntegerField(default=20, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True)
