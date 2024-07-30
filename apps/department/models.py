from django.db import models
from apps.employee.models import Employee


class Department(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    director: Employee = models.ForeignKey(
        'employee.Employee',
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
