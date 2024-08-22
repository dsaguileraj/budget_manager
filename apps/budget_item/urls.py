from django.urls import path
from . import views

app_name = "budget_item"

urlpatterns = [
    path("", views.list_budget_item, name="list"),
    path("create/", views.create_budget_item, name="create"),
    path("upload/", views.upload_file, name="upload"),
    path("<int:pk>/", views.detail_budget_item, name="detail"),
    path("delete/<int:pk>/", views.delete_budget_item, name="delete"),
    path("update/<int:pk>/", views.update_budget_item, name="update")
]
