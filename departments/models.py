from django.db import models


class Departments(models.Model):
    name = models.CharField(
        max_length = 255,
        primary_key = True
    )
    director = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
