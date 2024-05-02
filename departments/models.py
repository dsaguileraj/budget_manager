from django.db import models


class Employees(models.Model):
    ci = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    user = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.ci} - {self.name} {self.surname}"


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    director = models.ForeignKey(
        Employees,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
