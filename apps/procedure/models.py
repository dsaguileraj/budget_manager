from django.db import models
from apps.core.choices import ProductType, PurchaseType, Regime


class Procedure(models.Model):
    name: str = models.CharField(max_length=50)
    product_type: str = models.CharField(
        max_length=2,
        choices=ProductType.choices
    )
    purchase_type: str = models.CharField(
        max_length=1,
        blank=True,
        choices=PurchaseType.choices
    )
    regime: str = models.CharField(
        max_length=1,
        blank=True,
        choices=Regime.choices
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name', 'purchase_type', 'product_type', 'regime']
        ordering = ['name', 'purchase_type', 'product_type', 'regime']
