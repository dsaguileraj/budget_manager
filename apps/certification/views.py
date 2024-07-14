from rest_framework import permissions, viewsets
from .models import Certification
from .serializers import CertificationSerializer


class CertificactionViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
