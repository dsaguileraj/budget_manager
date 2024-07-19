from django.db import models
from django.core.validators import MinValueValidator
from apps.core.choices import BudgetType, PurchaseType
from apps.core.models import BaseModel


class BudgetItem(BaseModel):
    number = models.CharField(max_length=255)
    cpc = models.CharField(max_length=15)

    # Object of Contract
    description = models.TextField()
    activity = models.TextField()

    # Contability
    purchase_type = models.CharField(max_length=1, choices=PurchaseType)
    budget_type = models.CharField(max_length=2, choices=BudgetType)
    budget = models.DecimalField(max_digits=20, decimal_places=5, default=0.00001, validators=[
                                 MinValueValidator(0.00001)])
    # Period
    c1 = models.BooleanField(default=False)
    c2 = models.BooleanField(default=False)
    c3 = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.cpc}'

    class Meta:
        ordering = ['number', 'description', 'activity']
        unique_together = ['number', 'description', 'activity']
