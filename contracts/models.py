from django.db import models
from certifications.models import Certifications
from employees.models import Employees


class Contracts(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    certification = models.ForeignKey(
        Certifications,
        on_delete=models.DO_NOTHING
    )
    admin = models.ForeignKey(
        Employees,
        on_delete=models.DO_NOTHING
    )
    contractor = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.id
