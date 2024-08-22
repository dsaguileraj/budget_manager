from django.urls import path
from . import views

app_name = "procedure"

urlpatterns = [
    path("", views.list_procedure, name="list"),
    path("create/", views.create_procedure, name="create"),
    path("<int:pk>/", views.detail_procedure, name="detail"),
    path("delete/<int:pk>/", views.delete_procedure, name="delete"),
    path("update/<int:pk>/", views.update_procedure, name="update")
]
