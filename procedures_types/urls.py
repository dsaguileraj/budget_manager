from django.urls import path
from .views import *

app_name = "procedures_types"

urlpatterns = [
    path("", ProceduresTypesListView.as_view(), name = "list"),
    path("create/", create_procedure_type, name = "create"),
    path("<str:pk>/", ProceduresTypesDetailView.as_view(), name = "detail"),    
    path("delete/<str:pk>/", delete_procedure_type, name = "delete"),
    path("update/<str:pk>/", update_procedure_type, name = "update")
]
