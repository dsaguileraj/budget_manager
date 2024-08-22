from django.urls import path
from . import views

app_name = "contract"

urlpatterns = [
    path("", views.list_contract, name="list"),
    path("create/", views.create_contract, name="create"),
    path("<int:pk>/", views.detail_contract, name="detail"),
    path("delete/<int:pk>/", views.delete_contract, name="delete"),
    path("update/<int:pk>/", views.update_contract, name="update")
]
