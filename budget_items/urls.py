from django.urls import path
from .views import *

app_name = "budget_items"

urlpatterns = [
    path("", BudgetItemsListView.as_view(), name = "list"),
    path("create/", BudgetItemsCreateView.as_view(), name = "create"),
    path("<int:pk>/", BudgetItemsDetailView.as_view(), name = "detail"),    
    path("delete/<int:pk>/", BudgetItemsDeleteView.as_view(), name = "delete"),
    path("update/<int:pk>/", BudgetItemsUpdateView.as_view(), name = "update")
]
