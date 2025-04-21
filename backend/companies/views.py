from rest_framework import viewsets
from .models import TransportCompany
from .serializers import TransportCompanySerializer

class TransportCompanyViewSet(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer