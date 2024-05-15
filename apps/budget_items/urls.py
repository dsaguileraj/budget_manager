from django.urls import path
from .views import BudgetItemsListView, BudgetItemsDetailView, create_budget_item, delete_budget_item, update_budget_item, upload_file

app_name = "budget_items"

urlpatterns = [
    path("", BudgetItemsListView.as_view(), name="list"),
    path("create/", create_budget_item, name="create"),
    path("create/excel", upload_file, name="create_excel"),
    path("<int:pk>/", BudgetItemsDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", delete_budget_item, name="delete"),
    path("update/<int:pk>/", update_budget_item, name="update")
]
