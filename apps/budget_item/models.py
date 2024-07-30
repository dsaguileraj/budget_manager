from django.db import models
from django.core.validators import MinValueValidator
from apps.core.choices import BudgetType
from apps.core.models import AuditModel


class BudgetItem(AuditModel):
    number = models.CharField(max_length=255)
    cpc = models.CharField(max_length=15)

    # Object of Contract
    description = models.TextField()
    activity = models.TextField()

    # Contability
    budget = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    budget_type = models.CharField(
        max_length=2,
        choices=BudgetType.choices
    )
    bid = models.BooleanField(default=False)

    # Period
    c1 = models.BooleanField(default=False)
    c2 = models.BooleanField(default=False)
    c3 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.number} [{self.cpc}]'

    class Meta:
        ordering = ['number', 'description', 'activity']
        unique_together = ['number', 'description', 'activity']
