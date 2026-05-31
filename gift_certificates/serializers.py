from rest_framework import serializers
from .models import GiftCertificateOrder

class GiftCertificateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCertificateOrder
        fields = '__all__'