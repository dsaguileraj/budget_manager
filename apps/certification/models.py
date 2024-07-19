from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.budget_item.models import BudgetItem
from apps.department.models import Department
from apps.core.models import BaseModel
from apps.procedure.models import Procedure


class Certification(BaseModel):
    number = models.CharField(max_length=25)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    budget_item = models.ForeignKey(BudgetItem, on_delete=models.PROTECT)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT)
    description = models.TextField()
    budget = models.DecimalField(
        max_digits=20, decimal_places=5, default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.number} - {self.budget_item.number}'

    class Meta:
        ordering = ['number', 'budget_item', 'description']
        unique_together = ['number', 'budget_item']
