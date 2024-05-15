from django.db import models
from apps.employees.models import Employees


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    director = models.ForeignKey(
        Employees,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
