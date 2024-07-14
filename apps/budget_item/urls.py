from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetItemViewSet

router = DefaultRouter()
router.register(r'', BudgetItemViewSet)
urlpatterns = [
    path('', include(router.urls))
]
