from django.db import models


class Employee(models.Model):
    ci = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    first_last_name = models.CharField(max_length=50)
    middle_last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    user = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return {self.ci}

    class Meta:
        ordering = ['first_last_name', 'middle_last_name', 'first_name', 'middle_name', 'ci']
