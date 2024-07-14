from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, AdminHistorySerializer

router = DefaultRouter()

router.register(r'', ContractViewSet)
router.register(r'history', AdminHistorySerializer)

urlpatterns = [
    path('', include(router.urls))
]
