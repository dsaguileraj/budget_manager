from rest_framework import permissions, viewsets
from .models import BudgetItem
from .serializers import BudgetItemSerializer

class BudgetItemViewSet(viewsets.ModelViewSet):
    queryset = BudgetItem.objects.all()
    serializer_class = BudgetItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
