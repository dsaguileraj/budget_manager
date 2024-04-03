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
    budget_item = models.CharField(
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

    regime = models.CharField(max_length = 1)
    product_type = models.CharField(max_length = 2)
    purchase_type = models.CharField(max_length = 1)

    name = models.ForeignKey(
        ProceduresTypes,
        on_delete = models.CASCADE
    )

    def save(self, *args, **kwargs):
        proceduretype = ProceduresTypes.objects.get(pk = self.name_id)
        self.regime = proceduretype.regime
        self.product_type = proceduretype.product_type
        self.purchase_type = proceduretype.purchase_type
        super().save(*args, **kwargs)

    def __str__(self):
        return self.budget_item


class Certifications(models.Model):
    number = models.AutoField(primary_key = True)
    procedure = models.ForeignKey(
        ProceduresTypes,
        on_delete = models.CASCADE,
        related_name = "certifications_procedure"
    )
    department = models.ForeignKey(
        Departments,
        on_delete = models.CASCADE,
        related_name = "certifications_department"
    )
    date = models.DateTimeField(
        auto_now = True
    )
    budget = models.FloatField()
    description = models.TextField()
    period = models.IntegerField()

    cpc = models.CharField(max_length = 15)
    budget_type = models.CharField(max_length = 2, choices = BUDGET_TYPE_CHOICES)
    bid = models.BooleanField()

    regime = models.CharField(max_length = 1)
    product_type = models.CharField(max_length = 2)
    purchase_type = models.CharField(max_length = 1)

    budget_item_reference = models.ForeignKey(
        BudgetItems,
        on_delete = models.CASCADE
    )

    def save(self, *args, **kwargs):
        budget_item = BudgetItems.objects.get(pk = self.budget_item_reference_id)
        self.cpc = budget_item.cpc
        self.budget_type = budget_item.budget_type
        self.bid = budget_item.bid
        proceduretype = ProceduresTypes.objects.get(pk = budget_item.name_id)
        self.regime = proceduretype.regime
        self.product_type = proceduretype.product_type
        self.purchase_type = proceduretype.purchase_type
        super().save(*args, **kwargs)

    def __str__(self):
        return self.number
