from rest_framework import viewsets
from .models import GiftCertificateOrder
from .serializers import GiftCertificateOrderSerializer

class GiftCertificateViewSet(viewsets.ModelViewSet):
    queryset = GiftCertificateOrder.objects.all()
    serializer_class = GiftCertificateOrderSerializer