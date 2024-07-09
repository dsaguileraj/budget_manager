from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class BudgetType(TextChoices):
    CURRENT_EXPENSE = 'GC', _('Gasto Corriente')
    INVESTMENT_PROJECT = 'PI', _('Proyecto de Inversion')


class ProductType(TextChoices):
    NORMALIZED = 'N', _('Normalizado')
    NOT_NORMALIZED = '!N', _('No Normalizado')


class PurchaseType(TextChoices):
    GOOD = 'B', _('Bien')
    CONSULTING = 'C', _('Consultoría')
    CIVIL_WORK = 'O', _('Obra')
    SERVICE = 'S', _('Servicio')


class RegimeType(TextChoices):
    COMMON = 'C', _('Común')
    SPECIAL = 'E', _('Especial')
