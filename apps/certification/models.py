from django.db import models
from django.core.validators import MinValueValidator
from apps.budget_item.models import BudgetItem
from apps.department.models import Department
from apps.procedure.models import Procedure


class Certification(models.Model):
    number = models.CharField(
        max_length=25
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    budget_item = models.ForeignKey(
        BudgetItem,
        on_delete=models.CASCADE
    )
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    budget = models.DecimalField(
        max_digits=20,
        decimal_places=5,
        validators=[
            MinValueValidator(0.00001)
        ]
    )

    # Log
    create_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_update = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    # Docs
    certification = models.FileField(
        upload_to='certifications/'
    )
    resolution = models.FileField(
        upload_to='resolutions/',
        blank=True
    )

    def __str__(self):
        return f'{self.number} - {self.budget_item.number}'

    class Meta:
        ordering = ['number', 'budget_item', 'description']
        unique_together = ['number', 'budget_item']
