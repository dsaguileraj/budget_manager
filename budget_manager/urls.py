from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("budget_item/", include("apps.budget_item.urls")),
    path("certification/", include("apps.certification.urls")),
    path("contract/", include("apps.contract.urls")),
    path("department/", include("apps.department.urls")),
    path("employee/", include("apps.employee.urls")),
    path("procedure/", include("apps.procedure.urls")),
]
