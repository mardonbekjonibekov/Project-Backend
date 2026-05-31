from rest_framework import generics

from .models import DonationOption
from .serializers import DonationOptionSerializer


class DonationOptionListAPIView(generics.ListAPIView):
    serializer_class = DonationOptionSerializer

    def get_queryset(self):
        return DonationOption.objects.filter(is_active=True)
