from django.urls import path
from .views import list_certification, CertificationDetailView, create_certification, delete_certification, update_certification

app_name = "certification"

urlpatterns = [
    path("", list_certification, name="list"),
    path("create/", create_certification, name="create"),
    path("<int:pk>/", CertificationDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", delete_certification, name="delete"),
    path("update/<int:pk>/", update_certification, name="update")
]
