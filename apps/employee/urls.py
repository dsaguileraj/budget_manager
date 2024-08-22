from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path("", views.list_employee, name="list"),
    path("create/", views.create_employee, name="create"),
    path("<str:pk>/", views.detail_employee, name="detail"),
    path("delete/<str:pk>/", views.delete_employee, name="delete"),
    path("update/<str:pk>/", views.update_employee, name="update")
]
