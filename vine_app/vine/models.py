from django.db import models


# Create your models here.

class VineItem(models.Model):
    index=models.IntegerField(primary_key=True, default=0)
    inStock=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    picture=models.URLField(default="")
    year=models.IntegerField(default=0)
    color=models.CharField(max_length=10, default="")
    type_wine=models.CharField(max_length=40, default="")
    city=models.CharField(max_length=50, default="")
    name=models.CharField(max_length=50, default="")
    company=models.CharField(max_length=50, default="")
    about=models.TextField(default="")
    tags=models.TextField(default="")

    


