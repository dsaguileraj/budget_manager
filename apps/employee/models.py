from django.db import models


class Employee(models.Model):
    ci: str = models.CharField(primary_key=True, max_length=10)
    first_name: str = models.CharField(max_length=20)
    middle_name: str = models.CharField(max_length=20)
    first_last_name: str = models.CharField(max_length=20)
    middle_last_name: str = models.CharField(max_length=20)
    email: str = models.EmailField(max_length=100, unique=True)
    user: str = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.ci

    class Meta:
        ordering = [
            'first_last_name',
            'middle_last_name',
            'first_name',
            'middle_name',
            'ci'
        ]
