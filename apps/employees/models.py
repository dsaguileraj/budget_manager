from django.db import models


class Employees(models.Model):
    ci = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    user = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.ci} - {self.name} {self.surname}"
