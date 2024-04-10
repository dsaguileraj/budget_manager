from django.urls import path
from .views import Create, Delete, Detail, List, Update

app_name = "procedures_types"

urlpatterns = [
    path("", List.as_view(), name = "list"),
    path("create/", Create.as_view(), name = "create"),
    path("<str:pk>/", Detail.as_view(), name = "detail"),    
    path("delete/<str:pk>/", Delete.as_view(), name = "delete"),
    path("update/<str:pk>/", Update.as_view(), name = "update")
]
