"""
URL configuration for budget_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("budget_items/", include("apps.budget_items.urls")),
    path("certifications/", include("apps.certifications.urls")),
    path("departments/", include("apps.departments.urls")),
    path("procedures_types/", include("apps.procedures_types.urls")),
    path("employees/", include("apps.employees.urls")),
    path("contracts/", include("apps.contracts.urls")),
]
