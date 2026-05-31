from django.db import models

from events.models import Event


class CartItem(models.Model):
    ITEM_TYPES = [
        ("event", "Event"),
        ("gift_certificate", "Gift Certificate"),
        ("monthly_giving", "Monthly Giving"),
        ("donation", "Donation"),
    ]

    session_key = models.CharField(max_length=80, db_index=True)
    item_type = models.CharField(max_length=32, choices=ITEM_TYPES, default="event")
    item_name = models.CharField(max_length=180, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="cart_items", blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def line_total(self):
        return self.unit_price * self.quantity

    @property
    def label(self):
        if self.event_id:
            return self.event.title
        return self.item_name

    def __str__(self):
        return f"{self.label} x {self.quantity}"
