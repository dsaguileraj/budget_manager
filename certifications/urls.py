from django.urls import path
from .views import CertificationsListView, CertificationsDetailView, create_certification, delete_certification, update_certification

app_name = "certifications"

urlpatterns = [
    path("", CertificationsListView.as_view(), name="list"),
    path("create/", create_certification, name="create"),
    path("<int:pk>/", CertificationsDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", delete_certification, name="delete"),
    path("update/<int:pk>/", update_certification, name="update")
]
