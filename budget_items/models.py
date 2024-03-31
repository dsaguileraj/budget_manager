from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class HiringProcedureType(models.Model):
    REGIME_CHOICES = (
        ("common", "Común"),
        ("special", "Especial"),
        ("not_applicable", "No aplica"),
    )
    PRODUCT_TYPE_CHOICES = (
        ("normalized", "Normalizado"),
        ("not_normalized", "No normalizado"),
        ("not_applicable", "No aplica"),
    )
    regime = models.CharField(
        max_length = 255,
        choices = REGIME_CHOICES,
        default = "not_applicable",
    )
    product_type = models.CharField(
        max_length = 255,
        choices = PRODUCT_TYPE_CHOICES,
        default = "not_applicable",
    )
    procedure = models.CharField(
        max_length = 255
        )

    def __str__(self):
        return f"{self.regime} - {self.product_type}"
    

class BudgetItem(models.Model):
    PURCHASE_TYPE_CHOICES = (
        ('GOODS', 'Bienes'),
        ('SERVICES', 'Servicios'),
        ('WORKS', 'Obras'),
        ('CONSULTING', 'Consultoría'),
    )
    regime = models.ForeignKey(
        HiringProcedureType,
        on_delete = models.CASCADE,
        related_name = "budget_items_regime"
        )
    product_type = models.ForeignKey(
        HiringProcedureType,
        on_delete = models.CASCADE,
        related_name = "budget_items_product_type"
        )
    procedure = models.ForeignKey(
        HiringProcedureType,
        on_delete = models.CASCADE,
        related_name = "budget_items_procedure"
        )
    purchase_type = models.CharField(
        max_length = 255,
        choices = PURCHASE_TYPE_CHOICES
        )
    budget_item = models.CharField(
        max_length = 255
        )
    cpc = models.CharField(
        max_length = 15
        )
    date = models.DateTimeField(
        auto_now_add = True
        )
    budget = models.FloatField()
    description = models.TextField()
    period = models.IntegerField()
    bid = models.BooleanField()

    def __str__(self):
        return f"{self.budget_item} - {self.description}"
    

class Certification(models.Model):
    budget_item = models.ForeignKey(
        BudgetItem,
        on_delete = models.CASCADE,
        related_name = "certifications_budget_item"
        )
    cpc = models.ForeignKey(
        BudgetItem,
        on_delete = models.CASCADE,
        related_name = "certifications_cpc"
        )
    regime = models.ForeignKey(
        HiringProcedureType,
        on_delete = models.CASCADE,
        related_name = "certifications_regime"
        )
    product_type = models.ForeignKey(
        BudgetItem,
        on_delete = models.CASCADE,
        related_name = "certifications_product_type"
        )
    procedure = models.ForeignKey(
        HiringProcedureType,
        on_delete = models.CASCADE,
        related_name = "certifications_procedure"
        )
    department = models.ForeignKey(
        Department,
        on_delete = models.CASCADE,
        related_name = "certifications_department"
        )
    bid = models.ForeignKey(
        BudgetItem,
        on_delete = models.CASCADE,
        related_name = "certifications_bid"
    )
    purchase_type = models.CharField(
        max_length=255,
        choices = BudgetItem.PURCHASE_TYPE_CHOICES
        )
    date = models.DateTimeField(
        auto_now = True
        )    
    budget = models.FloatField()
    description = models.TextField()
    period = models.IntegerField()

    def __str__(self):
        return self.budget_item.budget_item



