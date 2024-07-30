from decimal import Decimal
from django.db import models
from apps.certification.models import Certification
from apps.employee.models import Employee
from apps.core.models import AuditModel


class Contract(AuditModel):
    number = models.CharField(
        max_length=30,
        unique=True
    )
    certification = models.ManyToManyField(Certification)
    admin: Employee = models.ForeignKey(
        'employee.Employee',
        on_delete=models.PROTECT
    )
    contractor = models.CharField(max_length=100)
    suscription = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.number

    @property
    def budget(self):
        return self.certification.aggregate(total=models.Sum('budget'))['total'] or 0

    class Meta:
        ordering = ['number']
