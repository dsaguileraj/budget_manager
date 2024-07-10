from django.db import models
from django.core.validators import MinValueValidator
from apps.certification.models import Certification
from apps.employee.models import Employee


class Contract(models.Model):
    number = models.CharField(
        primary_key=True,
        max_length=30,
    )
    certification = models.ForeignKey(
        Certification,
        on_delete=models.CASCADE
    )
    admin = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True
    )
    contractor = models.CharField(
        max_length=100
    )
    duration = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    date = models.DateField()

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
