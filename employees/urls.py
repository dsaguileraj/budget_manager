from django.urls import path
from .views import *

app_name = "employees"

urlpatterns = [
    path("", EmployeesListView.as_view(), name = "list"),
    path("create/", create_employee.as_view(), name = "create"),
    path("<str:pk>/", EmployeesDetailView.as_view(), name = "detail"),    
    path("delete/<str:pk>/", delete_employee.as_view(), name = "delete"),
    path("update/<str:pk>/", update_employee.as_view(), name = "update")
]
