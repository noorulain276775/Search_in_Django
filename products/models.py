from django.db import models

class Products(models.Model):
    name= models.CharField()
    category= models.CharField()
    brand= models.CharField()
    price= models.DecimalField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField()