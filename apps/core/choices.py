from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class BudgetType(TextChoices):
    GC = "Gasto Corriente", _("Gasto Corriente")
    PI = "Proyecto de Inversión", _("Proyecto de Inversión")


class ProductType(TextChoices):
    N = "Normalizado", _("Normalizado")
    NN = "No Normalizado", _("No Normalizado")


class PurchaseType(TextChoices):
    B = "Bien", _("Bien")
    C = "Consultoría", _("Consultoría")
    O = "Obra", _("Obra")
    S = "Servicio", _("Servicio")


class Regime(TextChoices):
    C = "Común", _("Común")
    E = "Especial", _("Especial")
