from rest_framework import generics

from .models import MonthlyGivingOption
from .serializers import MonthlyGivingOptionSerializer


class MonthlyGivingListAPIView(generics.ListAPIView):
    serializer_class = MonthlyGivingOptionSerializer

    def get_queryset(self):
        return MonthlyGivingOption.objects.filter(is_active=True)
