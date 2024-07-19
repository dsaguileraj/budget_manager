from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, AdminHistoryViewSet

router = DefaultRouter()

router.register(r'c', ContractViewSet)
router.register(r'h', AdminHistoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
