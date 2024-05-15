from django.db import models
from apps.budget_items.models import BudgetItems
from apps.departments.models import Departments
from apps.procedures_types.models import ProceduresTypes

PERIOD_CHOICES = (
    ("C1", "C1"),
    ("C2", "C3"),
    ("C3", "C3"),
    ("C1 - C2", "C1 - C2"),
    ("C1 - C3", "C1 - C3"),
    ("C2 - C3", "C2 - C3"),
    ("C1 - C2 - C3", "C1 - C2 - C3"),
)


class Certifications(models.Model):
    number = models.AutoField(
        primary_key=True
    )
    procedure = models.ForeignKey(
        ProceduresTypes,
        on_delete=models.CASCADE
    )
    budget_item = models.ForeignKey(
        BudgetItems,
        on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(
        auto_now=True
    )
    budget = models.FloatField()
    description = models.TextField()
    period = models.CharField(
        max_length=12,
        choices=PERIOD_CHOICES
    )

    def __str__(self):
        return self.number
