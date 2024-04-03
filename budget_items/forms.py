from django.forms import ModelForm
from .models import *


class CreateDepartment(ModelForm):
    class Meta:
        model = Department
        fields = ["__all__"]


class CreateBudgetItem(ModelForm):
    class Meta:
        model = BudgetItem
        fields = ["__all__"]
        


class CreateCertification(ModelForm):
    class Meta:
        model = Certification
        fields = ["__all__"]
