from django.db import models

PURCHASE_TYPE_CHOICES = (
    ("Good", "Good"),
    ("Service", "Service"),
    ("Work", "Work"),
    ("Consultancy", "Consultancy"),
    ("Goods & Services", "Goods & Services"),
)

REGIME_CHOICES = (
    ("Common", "Common"),
    ("Special", "Special"),
    ("Not Applicable", "Not Applicable")
)

PRODUCT_TYPE_CHOICES = (
    ("Normalized", "Normalized"),
    ("Not Normalized", "Not Normalized"),
    ("Not Applicable", "Not Applicable")
)


class ProceduresTypes(models.Model):
    id = models.AutoField(
        primary_key = True
    )
    name = models.CharField(
        max_length = 50
    )
    regime = models.CharField(
        max_length = 14,
        choices = REGIME_CHOICES
    )
    product_type = models.CharField(
        max_length = 14,
        choices = PRODUCT_TYPE_CHOICES
    )
    purchase_type = models.CharField(
        max_length = 16,
        choices = PURCHASE_TYPE_CHOICES
    )

    def __str__(self):
        return self.name
