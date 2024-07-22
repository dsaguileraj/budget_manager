from django.db import models
from apps.certification.models import Certification
from apps.core.models import BaseModel
from apps.employee.models import Employee


class Contract(BaseModel):
    number = models.CharField(max_length=25, unique=True)
    certification = models.ForeignKey(Certification, on_delete=models.PROTECT)
    admin = models.ForeignKey(Employee, on_delete=models.PROTECT)
    contractor = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
