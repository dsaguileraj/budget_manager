from django.urls import path
from .views import Create, Delete, Detail, List, Update

app_name = "certifications"

urlpatterns = [
    path("", List.as_view(), name = "list"),
    path("create/", Create.as_view(), name = "create"),
    path("<int:pk>/", Detail.as_view(), name = "detail"),    
    path("delete/<int:pk>/", Delete.as_view(), name = "delete"),
    path("update/<int:pk>/", Update.as_view(), name = "update")
]
