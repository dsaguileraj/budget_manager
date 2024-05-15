from django.db import models

PURCHASE_TYPE_CHOICES = (
    ("Bien", "Bien"),
    ("Servicio", "Servicio"),
    ("Obra", "Obra"),
    ("Consultoría", "Consultoría"),
    ("Bienes y Servicios", "Bienes y Servicios"),
)

REGIME_CHOICES = (
    ("Común", "Común"),
    ("Especial", "Especial"),
    ("No Aplica", "No Aplica")
)

PRODUCT_TYPE_CHOICES = (
    ("Normalizado", "Normalizado"),
    ("No Normalizado", "No Normalizado"),
    ("No Aplica", "No Aplica")
)


class ProceduresTypes(models.Model):
    id = models.AutoField(
        primary_key = True
    )
    name = models.CharField(
        max_length = 50
    )
    regime = models.CharField(
        max_length = 9,
        choices = REGIME_CHOICES
    )
    product_type = models.CharField(
        max_length = 14,
        choices = PRODUCT_TYPE_CHOICES
    )
    purchase_type = models.CharField(
        max_length = 18,
        choices = PURCHASE_TYPE_CHOICES
    )

    def __str__(self):
        return self.name
