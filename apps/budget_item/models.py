from django.db import models
from django.core.validators import MinValueValidator
from apps.core.choices import BudgetType
from apps.core.models import AuditModel


class BudgetItem(AuditModel):
    number: str = models.CharField(max_length=255)
    cpc: str = models.CharField(max_length=15)

    # Object of Contract
    description: str = models.TextField()
    activity: str = models.TextField()

    # Contability
    budget: float = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    budget_type: str = models.CharField(
        max_length=2,
        choices=BudgetType.choices
    )
    bid: bool = models.BooleanField(default=False)

    # Period
    c1: bool = models.BooleanField(default=False)
    c2: bool = models.BooleanField(default=False)
    c3: bool = models.BooleanField(default=False)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number', 'description', 'activity']
        unique_together = ['number', 'description', 'activity']
