from decimal import Decimal
from django.db import models
from apps.certification.models import Certification
from apps.employee.models import Employee
from apps.core.models import AuditModel


class Contract(AuditModel):
    number = models.CharField(max_length=30, unique=True)
    certification = models.ManyToManyField(Certification)
    admin = models.ForeignKey(Employee, on_delete=models.PROTECT)
    contractor = models.CharField(max_length=100)
    description = models.TextField()
    suscription = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.number

    @property
    def total_budget(self) -> Decimal | int:
        return self.certification.aggregate(total=models.Sum("budget"))["total"] or 0

    class Meta:
        ordering = ["number"]
