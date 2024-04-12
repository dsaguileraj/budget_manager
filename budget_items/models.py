from django.db import models

BUDGET_TYPE_CHOICES = (
    ("CE", "Current Expense"),
    ("IP", "Investment Project")
)


class BudgetItems(models.Model):
    budget_item_id = models.AutoField(
        primary_key = True
    )
    number = models.CharField(
        max_length = 255
    )
    cpc = models.CharField(
        max_length = 15
    )
    date = models.DateTimeField(
        auto_now_add = True
    )
    budget = models.FloatField()
    budget_type = models.CharField(
        max_length = 2,
        choices = BUDGET_TYPE_CHOICES
    )
    description = models.TextField()
    bid = models.BooleanField()

    def __str__(self):
        return self.number