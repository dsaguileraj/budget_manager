from django.db import models

PURCHASE_TYPE_CHOICES = (
    ("G", "Good"),
    ("S", "Service"),
    ("W", "Work"),
    ("C", "Consultancy")
)

REGIME_CHOICES = (
    ("C", "Common"),
    ("S", "Speciall"),
    ("N", "Not Applicable")
)

PRODUCT_TYPE_CHOICES = (
    ("N", "Normalized"),
    ("NN", "Not Normalized"),
    ("NA", "Not Applicable")
)


class ProceduresTypes(models.Model):
    name = models.CharField(
        max_length = 50,
        primary_key = True
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
