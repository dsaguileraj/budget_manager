from django.db import models


BUDGET_TYPE_CHOICES = (
    ("Gasto Corriente", "Gasto Corriente"),
    ("Proyecto de Inversión", "Proyecto de Inversión")
)


class BudgetItems(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    number = models.CharField(
        max_length=255
    )
    cpc = models.CharField(
        max_length=15
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    budget = models.FloatField()
    budget_type = models.CharField(
        max_length=21,
        choices=BUDGET_TYPE_CHOICES
    )
    description = models.TextField()
    activity = models.TextField()
    bid = models.BooleanField()

    def __str__(self):
        return self.number