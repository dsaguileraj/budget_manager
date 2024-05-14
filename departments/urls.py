from django.urls import path
from .views import DepartmentsListView, DepartmentsDetailView, create_department, delete_department, update_department

app_name = "departments"

urlpatterns = [
    path("", DepartmentsListView.as_view(), name="list"),
    path("create/", create_department, name="create"),
    path("<str:pk>/", DepartmentsDetailView.as_view(), name="detail"),
    path("delete/<str:pk>/", delete_department, name="delete"),
    path("update/<str:pk>/", update_department, name="update")
]
