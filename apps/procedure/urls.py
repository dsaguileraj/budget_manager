from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcedureViewSet

router = DefaultRouter()
router.register(r'', ProcedureViewSet)
urlpatterns = [
    path('', include(router.urls))
]
