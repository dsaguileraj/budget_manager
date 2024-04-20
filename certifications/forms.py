from django.forms import ModelForm
from .models import Certifications

class CertificationsForm(ModelForm):
    class Meta:
        model = Certifications
        fields = ["budget_item", "description", "department", "budget", "procedure", "period"]