from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    date_range = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "starts_at",
            "ends_at",
            "date_range",
            "short_description",
            "long_description",
            "price",
            "image",
            "visual_style",
            "button_label",
            "is_active",
            "display_order",
        ]

    def get_date_range(self, obj):
        start = obj.starts_at.strftime("%a %B %d, %Y")
        end = obj.ends_at.strftime("%a %B %d, %Y")
        return f"{start} - {end}"
