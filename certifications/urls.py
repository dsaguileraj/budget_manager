from django.urls import path
from .views import *

app_name = "certifications"

urlpatterns = [
    path("", CertificationsListView.as_view(), name = "list"),
    path("create/", create_certification, name = "create"),
    path("<int:pk>/", CertificationsDetailView.as_view(), name = "detail"),    
    path("delete/<int:pk>/", CertificationsDeleteView.as_view(), name = "delete"),
    path("update/<int:pk>/", CertificationsUpdateView.as_view(), name = "update")
]
