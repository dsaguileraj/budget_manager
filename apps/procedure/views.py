from rest_framework import permissions, viewsets
from .models import Procedure
from .serializers import ProcedureSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
