from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class OtherProducts(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Other Product'
        verbose_name_plural = 'Other Products'