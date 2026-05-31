from rest_framework import serializers

from events.models import Event
from events.serializers import EventSerializer

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.filter(is_active=True),
        source="event",
        write_only=True,
        required=False,
    )
    amount = serializers.DecimalField(max_digits=8, decimal_places=2, write_only=True, required=False)
    label = serializers.CharField(read_only=True)
    line_total = serializers.DecimalField(max_digits=9, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = [
            "id",
            "item_type",
            "item_name",
            "label",
            "event",
            "event_id",
            "quantity",
            "unit_price",
            "amount",
            "line_total",
            "created_at",
        ]
        read_only_fields = ["id", "unit_price", "line_total", "created_at"]

    def create(self, validated_data):
        request = self.context["request"]
        if not request.session.session_key:
            request.session.create()
        quantity = validated_data.get("quantity", 1)

        event = validated_data.get("event")
        if event:
            lookup = {"session_key": request.session.session_key, "event": event}
            defaults = {
                "quantity": quantity,
                "unit_price": event.price,
                "item_type": "event",
                "item_name": event.title,
            }
            price = event.price
        else:
            item_name = validated_data.get("item_name", "").strip()
            amount = validated_data.get("amount")
            item_type = validated_data.get("item_type", "donation")
            if not item_name or amount is None:
                raise serializers.ValidationError("item_name and amount are required for non-event cart items.")
            lookup = {
                "session_key": request.session.session_key,
                "event__isnull": True,
                "item_type": item_type,
                "item_name": item_name,
                "unit_price": amount,
            }
            defaults = {"quantity": quantity}
            price = amount

        item, created = CartItem.objects.get_or_create(**lookup, defaults=defaults)
        if not created:
            item.quantity += quantity
            item.unit_price = price
            item.save(update_fields=["quantity", "unit_price", "updated_at"])
        return item


class CartSummarySerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)
    count = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=9, decimal_places=2)
