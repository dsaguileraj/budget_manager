from datetime import date
from django.db import models
from apps.certification.models import Certification
from apps.employee.models import Employee
from apps.core.models import AuditModel


class Contract(AuditModel):
    number: str = models.CharField(
        max_length=30,
        unique=True
    )
    certification: Certification = models.ManyToManyField(
        'certification.Certification')
    admin: Employee = models.ForeignKey(
        'employee.Employee',
        on_delete=models.PROTECT
    )
    contractor: str = models.CharField(max_length=100)
    suscription: date = models.DateField()
    duration: int = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.number

    class Meta:
        ordering = ['number']
