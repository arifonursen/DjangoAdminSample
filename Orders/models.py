from django.contrib.auth.models import User
from django.db import models

from Products.models import Products


class Orders(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    orderQty = models.IntegerField()
    orderDate = models.DateTimeField()
    orderCategory = models.CharField(choices=(('Phone', 'Phone'), ('Computer', 'Computer'), ('Television', 'Television')), max_length=50)
    orderCity = models.CharField(choices=(('Istanbul', 'Istanbul'), ('Ankara', 'Ankara')), max_length=150)
    productPrice = models.IntegerField(default=0)
    orderTotal = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
