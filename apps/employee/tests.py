from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.employee.models import Employee


class EmployeeTest(TestCase):
    def setUp(self) -> None:
        """Initial instance"""
        self.employee = Employee(
            ci="1234567890",
            name="Jhon",
            last_name="Doe",
            email="example@example.com",
            user="JHON_DOE"
        )
        self.employee.save()
        self.assertEqual(self.employee.ci, "1234567890")
        self.assertEqual(self.employee.name, "Jhon")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.email, "example@example.com",)
        self.assertEqual(self.employee.user, "JHON_DOE")

    def test_invalid_ci(self):
        """Invalidad CI"""
        with self.assertRaises(ValidationError):
            invalidad_employee = Employee(
                ci="12345678901",
                name="Jhon",
                last_name="Doe",
                email="example3@example.com",
                user="JHON_DOE3"
            )
            invalidad_employee.save()

    def test_duplicate_user(self):
        """Duplicate user"""
        with self.assertRaises(ValidationError):
            invalidad_employee = Employee(
                ci="2345678901",
                name="Jhon",
                last_name="Doe",
                email="example222@example.com",
                user="JHON_DOE"
            )
            invalidad_employee.save()

    def test_duplicate_email(self):
        """Duplicate email"""
        with self.assertRaises(ValidationError):
            invalidad_employee = Employee(
                ci="3456789012",
                name="Jhon",
                last_name="Doe",
                email="example@example.com",
                user="JHON_DOE2"
            )
            invalidad_employee.save()
