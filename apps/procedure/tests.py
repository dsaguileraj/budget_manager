from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.core.choices import ProductType, PurchaseType, RegimeType
from apps.procedure.models import Procedure


class ProcedureTest(TestCase):
    def setUp(self) -> None:
        """Initial instance"""
        self.procedure = Procedure(
            name="Procedure A",
            regime=RegimeType.COMMON,
            product_type=ProductType.NORMALIZED,
            purchase_type=PurchaseType.GOOD,
        )
        self.procedure.save()
        self.assertEqual(self.procedure.name, "Procedure A")
        self.assertEqual(self.procedure.regime, RegimeType.COMMON)
        self.assertEqual(self.procedure.product_type, ProductType.NORMALIZED)
        self.assertEqual(self.procedure.purchase_type, PurchaseType.GOOD)

    def test_unique_together_success(self) -> None:
        """Procedures with same name but different fields"""
        first_duplicate_procedure = Procedure(
            name="Procedure A",
            regime=RegimeType.COMMON,
            product_type=ProductType.NORMALIZED,
            purchase_type=PurchaseType.SERVICE,
        )
        first_duplicate_procedure.save()
        second_duplicate_procedure = Procedure(
            name="Procedure A",
            regime=RegimeType.COMMON,
            product_type=ProductType.NOT_NORMALIZED,
            purchase_type=PurchaseType.SERVICE,
        )
        second_duplicate_procedure.save()
        third_duplicate_procedure = Procedure(
            name="Procedure A",
            regime=RegimeType.SPECIAL,
            product_type=ProductType.NORMALIZED,
            purchase_type=PurchaseType.SERVICE,
        )
        third_duplicate_procedure.save()

    def test_unique_together_fail(self) -> None:
        """Procedure with same fields"""
        with self.assertRaises(ValidationError):
            duplicate_procedure = Procedure(
                name="Procedure A",
                regime=RegimeType.COMMON,
                product_type=ProductType.NORMALIZED,
                purchase_type=PurchaseType.GOOD,
            )
            duplicate_procedure.save()
