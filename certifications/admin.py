from django.contrib import admin
from .models import Certifications, CertificationsBudgetItems

admin.site.register([Certifications, CertificationsBudgetItems])
