from django.db import models
from apps.core.choices import ProductType, PurchaseType, RegimeType


class Procedure(models.Model):
    name = models.CharField(max_length=50)
    regime = models.CharField(max_length=1, null=True,
                              default=None, choices=RegimeType)
    product_type = models.CharField(
        max_length=2, null=True, default=None, choices=ProductType)
    purchase_type = models.CharField(max_length=1, choices=PurchaseType)

    def __str__(self):
        return f'{self.name} - {self.purchase_type}'

    class Meta:
        ordering = ['name', 'purchase_type']
        unique_together = ['name', 'regime', 'product_type', 'purchase_type']
