from django.db import models

PURCHASE_TYPE_CHOICES = (
    ("G", "Good"),
    ("S", "Service"),
    ("W", "Work"),
    ("C", "Consultancy"),
    ("-", "Goods & Services"),
)

REGIME_CHOICES = (
    ("C", "Common"),
    ("S", "Special"),
    ("N", "Not Applicable")
)

PRODUCT_TYPE_CHOICES = (
    ("N", "Normalized"),
    ("NN", "Not Normalized"),
    ("NA", "Not Applicable")
)


class ProceduresTypes(models.Model):
    id = models.AutoField(
        primary_key = True
    )
    name = models.CharField(
        max_length = 50
    )
    regime = models.CharField(
        max_length = 1,
        choices = REGIME_CHOICES
    )
    product_type = models.CharField(
        max_length = 2,
        choices = PRODUCT_TYPE_CHOICES
    )
    purchase_type = models.CharField(
        max_length = 1,
        choices = PURCHASE_TYPE_CHOICES
    )

    def __str__(self):
        return self.name
