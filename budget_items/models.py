from django.db import models

PURCHASE_TYPE_CHOICES = (
    ("B", "Bienes"),
    ("S", "Servicios"),
    ("O", "Obras"),
    ("C", "Consultoría")
)

REGIME_CHOICES = (
    ("C", "Común"),
    ("S", "Especial"),
    ("N", "No Aplica")
)

PRODUCT_TYPE_CHOICES = (
    ("N", "Normalizado"),
    ("NN", "No Normalizado"),
    ("NA", "No Aplica")
)

BUDGET_TYPE_CHOICES = (
    ("GC", "Gasto Corriente"),
    ("PI", "Proyecto de Inversión")
)


class Departments(models.Model):
    name = models.CharField(
        max_length = 255,
        primary_key = True
    )
    director = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class ProceduresTypes(models.Model):
    name = models.CharField(
        max_length = 50,
        primary_key = True
    )
    regime = models.CharField(
        max_length = 1,
        choices = REGIME_CHOICES
    )
    product_type = models.CharField(
        max_length = 2,
        choices = PRODUCT_TYPE_CHOICES
    )
    purchase_type = models.CharField(
        max_length = 1,
        choices = PURCHASE_TYPE_CHOICES
    )

    def __str__(self):
        return self.name


class BudgetItems(models.Model):
    number = models.CharField(
        max_length = 255,
        primary_key = True
    )
    cpc = models.CharField(
        max_length = 15
    )
    date = models.DateTimeField(
        auto_now_add = True
    )
    budget = models.FloatField()
    budget_type = models.CharField(
        max_length = 2,
        choices = BUDGET_TYPE_CHOICES
    )
    description = models.TextField()
    bid = models.BooleanField()

    def __str__(self):
        return self.number


class Certifications(models.Model):
    number = models.AutoField(
        primary_key = True
    )
    
    procedure = models.ForeignKey(
        ProceduresTypes,
        on_delete = models.CASCADE
    )
    budget_item = models.ForeignKey(
        BudgetItems,
        on_delete = models.CASCADE
    )
    department = models.ForeignKey(
        Departments,
        on_delete = models.CASCADE
    )
    
    date = models.DateTimeField(
        auto_now = True
    )
    budget = models.FloatField()
    description = models.TextField()
    period = models.IntegerField()

    def __str__(self):
        return self.number
