from django.urls import path
from .views import EmployeesListView, EmployeesDetailView, create_employee, delete_employee, update_employee

app_name = "employees"

urlpatterns = [
    path("", EmployeesListView.as_view(), name="list"),
    path("create/", create_employee, name="create"),
    path("<str:pk>/", EmployeesDetailView.as_view(), name="detail"),
    path("delete/<str:pk>/", delete_employee, name="delete"),
    path("update/<str:pk>/", update_employee, name="update")
]
