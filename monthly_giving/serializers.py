from rest_framework import serializers

from .models import MonthlyGivingOption


class MonthlyGivingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyGivingOption
        fields = ["id", "title", "amount", "description", "is_featured", "is_active", "display_order"]
