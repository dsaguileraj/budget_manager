from django.urls import path
from .views import *

app_name = "departments"

urlpatterns = [
    path("", DepartmentsListView.as_view(), name = "list"),
    path("create/", DepartmentsCreateView.as_view(), name = "create"),
    path("<str:pk>/", DepartmentsDetailView.as_view(), name = "detail"),    
    path("delete/<str:pk>/", DepartmentsDeleteView.as_view(), name = "delete"),
    path("update/<str:pk>/", DepartmentsUpdateView.as_view(), name = "update")
]
