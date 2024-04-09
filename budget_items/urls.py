from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "index"),
    path("budget_items/", BudgetItemsListView.as_view(), name = "budget_items"),
    path("budget_items/<str:pk>", BudgetItemsDetalView.as_view(), name = "detail_budget_item"),
    path("budget_items/create", BudgetItemsCreateView.as_view(), name = "create_budget_item"),    
    path("budget_items/delete/<str:pk>", BudgetItemsDeleteView.as_view(), name = "delete_budget_item"),
    path("certifications/", CertificationsListView.as_view(), name = "certifications"),
    path("certifications/<int:pk>", CertificationsDetailView.as_view(), name = "detail_certification"),
    path("certifications/create", CertificationsCreateView.as_view(), name = "create_certification"),
    path("certifications/delete/<int:pk>", CertificationsDeleteView.as_view(), name = "delete_certification"),
    path("departments/", DepartmentsListView.as_view(), name = "departments"),
    path("departments/<str:pk>", DepartmentsDetailView.as_view(), name = "detail_department"),
    path("departments/create", DepartmentsCreateView.as_view(), name = "create_department"),
    path("departments/delete/<str:pk>", DepartmentsDeleteView.as_view(), name = "delete_department"),
    path("procedures_types/", ProceduresTypesListView.as_view(), name = "procedures_types"),
    path("procedures_types/<str:pk>", ProceduresTypesDetailView.as_view(), name = "detail_procedure_type"),
    path("procedures_types/create", ProceduresTypesCreateView.as_view(), name = "create_procedure_type"),
    path("procedures_types/delete/<str:pk>", ProceduresTypesDeleteView.as_view(), name = "delete_procedure_type"),
]