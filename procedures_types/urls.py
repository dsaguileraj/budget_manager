from django.urls import path
from .views import *

app_name = "procedures_types"

urlpatterns = [
    path("", ProceduresTypesListView.as_view(), name = "list"),
    path("create/", ProceduresTypesCreateView.as_view(), name = "create"),
    path("<str:pk>/", ProceduresTypesDetailView.as_view(), name = "detail"),    
    path("delete/<str:pk>/", delete_procedure_type, name = "delete"),
    path("update/<str:pk>/", ProceduresTypesUpdateView.as_view(), name = "update")
]
