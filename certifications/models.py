from django.db import models
from budget_items.models import BudgetItems
from departments.models import Departments
from procedures_types.models import ProceduresTypes

class Certifications(models.Model):
    number = models.AutoField(
        primary_key = True
    )
    procedure = models.ForeignKey(
        ProceduresTypes,
        on_delete = models.CASCADE
    )
    budget_item = models.ForeignKey(
        BudgetItems,
        on_delete = models.CASCADE
    )
    department = models.ForeignKey(
        Departments,
        on_delete = models.CASCADE
    )

    date = models.DateTimeField(
        auto_now = True
    )
    budget = models.FloatField()
    description = models.TextField()
    period = models.IntegerField()

    def __str__(self):
        return self.number
