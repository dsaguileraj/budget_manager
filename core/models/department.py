from django.db import models
from core.models.employee import Employee

class Department(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    director = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
