from rest_framework import permissions, viewsets
from .models import Contract, AdminHistory
from .serializers import ContractSerializer, AdminHistorySerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdminHistoryViewSet(viewsets.ModelViewSet):
    queryset = AdminHistory.objects.all()
    serializer_class = AdminHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
