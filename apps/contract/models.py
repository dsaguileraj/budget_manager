from django.db import models
from apps.certification.models import Certification
from apps.core.models import BaseModel
from apps.employee.models import Employee


class Contract(BaseModel):
    number = models.CharField(primary_key=True, max_length=30)
    certification = models.ForeignKey(
        Certification, on_delete=models.PROTECT)
    contractor = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
    contract = models.FileField(upload_to='contracts/', max_length=1)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']


class AdminHistory(BaseModel):
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    admin = models.ForeignKey(Employee, on_delete=models.PROTECT)
    resolution = models.FileField(upload_to='resolutions/', max_length=1)

    class Meta:
        ordering = ['created_at']
