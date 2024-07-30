from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class BudgetType(TextChoices):
    GC = 'GC', _('Gasto Corriente')
    PI = 'PI', _('Proyecto de Inversión')


class ProductType(TextChoices):
    N = 'N', _('Normalizado')
    NN = '!N', _('No Normalizado')


class PurchaseType(TextChoices):
    B = 'B', _('Bien')
    C = 'C', _('Consultoría')
    O = 'O', _('Obra')
    S = 'S', _('Servicio')


class Regime(TextChoices):
    C = 'C', _('Común')
    E = 'E', _('Especial')
