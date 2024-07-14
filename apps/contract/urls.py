from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, AdminHistoryViewSet

router = DefaultRouter()

router.register(r'', ContractViewSet)
router.register(r'history', AdminHistoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
