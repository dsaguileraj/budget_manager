from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificactionViewSet

router = DefaultRouter()
router.register(r'', CertificactionViewSet)
urlpatterns = [
    path('', include(router.urls))
]
