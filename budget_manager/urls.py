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
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', include_docs_urls(title='Budget Manager API')),
    path('api/budget_item/', include('apps.budget_item.urls')),
    path('api/certification/', include('apps.certification.urls')),
    path('api/contract/', include('apps.contract.urls')),
    path('api/department/', include('apps.department.urls')),
    path('api/employee/', include('apps.employee.urls')),
    path('api/procedure/', include('apps.procedure.urls')),
]
