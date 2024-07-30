from django.db import models
from django.core.validators import MinValueValidator
from apps.budget_item.models import BudgetItem
from apps.department.models import Department
from apps.procedure.models import Procedure
from apps.core.models import AuditModel


class Certification(AuditModel):
    number = models.CharField(max_length=25)
    department: Department = models.ForeignKey(
        'department.Department',
        on_delete=models.PROTECT
    )
    budget_item: BudgetItem = models.ForeignKey(
        'budget_item.BudgetItem',
        on_delete=models.PROTECT
    )
    procedure: Procedure = models.ForeignKey(
        'procedure.Procedure',
        on_delete=models.PROTECT
    )
    description = models.TextField()
    budget = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self) -> str:
        return f'{self.number} [{self.budget_item.number}]'

    class Meta:
        ordering = ['number', 'budget_item', 'description']
        unique_together = ['number', 'budget_item']
