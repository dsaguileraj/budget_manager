from rest_framework import permissions, viewsets
from .models import Contract
from .serializers import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
