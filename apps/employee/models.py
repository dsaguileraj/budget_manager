from django.db import models


class Employee(models.Model):
    ci = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    first_last_name = models.CharField(max_length=20)
    middle_last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    user = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.ci

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.first_last_name} {self.middle_last_name}'

    class Meta:
        ordering = ['first_last_name', 'middle_last_name',
                    'first_name', 'middle_name', 'ci']
