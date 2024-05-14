from django.urls import path
from .views import ContractsListView, ContractsDetailView, create_contract, delete_contract, update_contract

app_name = "contracts"

urlpatterns = [
    path("", ContractsListView.as_view(), name="list"),
    path("create/", create_contract, name="create"),
    path("<str:pk>/", ContractsDetailView.as_view(), name="detail"),
    path("delete/<str:pk>/", delete_contract, name="delete"),
    path("update/<str:pk>/", update_contract, name="update")
]
